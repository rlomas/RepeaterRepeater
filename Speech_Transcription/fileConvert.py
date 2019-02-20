from pydub import AudioSegment
from channel_sep import save_wav_channel
# from mp3toflac import convert_mp3
import sys
import wave

filename = sys.argv[1]
if not filename.endswith('.flac'):
    # if filename.endswith('.mp3'):
    #     print("Converting .mp3 to .flac")
    #     wav = wave.open(filename)
    #     save_wav_channel(filename, wav, 0)
    #     convert_mp3(filename)
    #     sys.exit(2)
    if filename.endswith('.wav'):
        print("Creating .flac copy of " + filename)
        wav = wave.open(filename)
        save_wav_channel(filename, wav, 0)
        song = AudioSegment.from_wav(filename)
        filename_no_ext = filename[:filename.find('.')]
        new_filename = filename_no_ext + '.flac'
        song.export(new_filename,format = "flac")
        sys.exit(2)
    else:
        sys.exit(1)
sys.exit(0)