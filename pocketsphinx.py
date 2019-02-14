from pocketsphinx import AudioFile

config = {
    'audio_file': 'record-2-5-2019_1-07-13.wav',   
}

print(AudioFile(**config))




