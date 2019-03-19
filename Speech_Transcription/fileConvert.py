from pydub import AudioSegment
import sys
import wave

filename = sys.argv[1]
if not filename.endswith('.flac'):
    if filename.endswith('.wav'):
        print("Creating .flac copy of " + filename)
        song = AudioSegment.from_wav(filename)
        filename_no_ext = filename[:filename.find('.')]
        new_filename = filename_no_ext + '.flac'
        song.export(new_filename,format = "flac")
        sys.exit(2)
    else:
        print("Filename doesn't start with .flac or .wav")
        sys.exit(1)
sys.exit(0)