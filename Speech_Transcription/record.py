import pyaudio
import wave
import time
from squid import *
from button import *
from enum import Enum


# globals
form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 10 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file

class Mode(Enum):
    GOOGLE = 1
    ALEXA = 2
    SIRI = 3


class Record(object):
    
    def __init__(self, cur_mode):
        self.audio = pyaudio.PyAudio()
        self.frames = []
        self.stream = None
        self.light = Squid(18,23,24)
        self.button_record = Button(25)
        self.button_mode = Button(16)
        self.time_elapsed = None

        if cur_mode == "OK Google. ":
            self.mode = Mode.GOOGLE
            self.light.set_color(BLUE)
        elif cur_mode == "Alexa. ":
            self.mode = Mode.ALEXA
            self.light.set_color([100,65,0])
        else:
            self.mode = Mode.SIRI
            self.light.set_color(PURPLE)
        
    def change_color(self):
        if self.mode == Mode.GOOGLE:
            self.light.set_color([100,65,0])
            self.mode = Mode.ALEXA
        elif self.mode == Mode.ALEXA:
            self.light.set_color(PURPLE)
            self.mode = Mode.SIRI
        elif self.mode == Mode.SIRI:
            self.light.set_color(BLUE)
            self.mode = Mode.GOOGLE
            
    def run_loop(self):
        while True:
            if self.button_record.is_pressed():
                # starts recording
                #print("recording begins")
                self.time_elapsed = time.time()
                self.light.set_color(RED)
                self.record()
                break
            elif self.button_mode.is_pressed():
                #print("button pressed")
                self.change_color()
                time.sleep(2)
                
    
    
                    
                    
            
    def open_stream(self):
        self.stream = self.audio.open(format=form_1,
                                      rate=44100,
                                      channels=chans,
                                      input_device_index=2,
                                      input=True,
                                      frames_per_buffer=chunk)

    def record(self):

        self.open_stream()

        while True:
            if self.button_record.is_pressed():
                self.time_elapsed = time.time() - self.time_elapsed
                #print("recording time: " + str(self.time_elapsed))
                #print("end recording")
                self.save()
                self.light.set_color(GREEN)
                break

            data = self.stream.read(chunk, exception_on_overflow=False)
            self.frames.append(data)

    def save(self):
        # stop the stream, close it, and terminate the pyaudio instantiation
        self.stream.stop_stream()
        self.stream.close()

        # save the audio frames as .wav file
        wavefile = wave.open(wav_output_filename,'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(self.audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(self.frames))
        wavefile.close()
        #print("saved file ")

def main():
    cur_mode = sys.argv[1]
    rec = Record(cur_mode)
    rec.run_loop()
    rec.audio.terminate()
    with open('currentMode.txt', 'w') as outfile:
        if rec.mode == Mode.GOOGLE:
            outfile.write("OK Google. ") 
        elif rec.mode == Mode.ALEXA:
            outfile.write("Alexa. ")
        else:
            outfile.write("Hey Siri. ")

if __name__ == "__main__":
    main()
