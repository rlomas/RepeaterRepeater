import pyaudio
import wave
import time
from squid import *
from button import *


# globals
form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 10 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file


class Record(object):
    
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.frames = []
        self.stream = None
        self.light = Squid(18,23,24)
        self.light.set_color(GREEN)
        self.button = Button(25)
        self.time_elapsed = None

    def run_loop(self):
        while True:
            if self.button.is_pressed():
                # starts recording
                print("recording begins")
                self.time_elapsed = time.time()
                self.light.set_color(RED)
                self.record()
                break

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
            if self.button.is_pressed():
                self.time_elapsed = time.time() - self.time_elapsed
                print("recording time: " + str(self.time_elapsed))
                print("end recording")
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
        print("saved file ")


if __name__ == "__main__":
    rec = Record()
    rec.run_loop()
    rec.audio.terminate()

