
import sys
import csv
import argparse
import os
import io
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


parser = argparse.ArgumentParser()
parser.add_argument('--input_file', type=str, help='Input audio file. Must be .flac')

def main():

	args = parser.parse_args()
	input_path = args.input_file

	transcribe_file(input_path)



def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    try:
        client = speech.SpeechClient()
    except:
        print("authentication needed")
        exit(1)

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        model="command_and_search",
        language_code='en-US',
        )
    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))


if __name__ == '__main__':
    
    main()
