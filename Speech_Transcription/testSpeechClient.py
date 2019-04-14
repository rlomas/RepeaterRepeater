from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

#client = speech_v1.SpeechClient(credentials="/Users/ajeetseenivasan/Downloads/repeaterrepeater-1550350494511-89146ac39d95.json")
#client = speech_v1.SpeechClient()
client = speech_v1.SpeechClient().from_service_account_file("raspberry-pi-key.json") 


encoding = enums.RecognitionConfig.AudioEncoding.FLAC
sample_rate_hertz = 44100
language_code = 'en-US'
config = {'encoding': encoding, 'sample_rate_hertz': sample_rate_hertz, 'language_code': language_code, 'max_alternatives': 10}
uri = 'gs://test-repeater-repeater/what_time_is_it.flac'
audio = {'uri': uri}

response = client.recognize(config, audio)

print(response)