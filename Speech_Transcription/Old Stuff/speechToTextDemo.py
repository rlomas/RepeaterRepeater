import sys
import csv
import argparse
import math
import numpy as np
from scipy.spatial import distance
import scipy as sci
from gtts import gTTS
import os
import subprocess
import speech_recognition as sr
import re
 
def say(text):
    subprocess.call('say ' + text, shell=True)


def main():
	#print("hello")
	# tts = gTTS('Whats the weather like?')
	# dir = os.path.dirname(os.path.realpath(__file__))
	# tts.save(os.path.join(dir,'helloFile.mp3'))

	phrase_list = ["Alexa, how do you make pizza","Alexa, will it rain today","Alexa, whats in the news","Alexa, wake me up everyday at 9am"
	,"Alexa, sing me a song","Alexa, flip a coin","pizza","coin","news","song","rain"]
	file_list = ["Alexa-pizza.wav","Alexa-rain.wav","Alexa-news.wav","Alexa-9am.wav","Alexa-song.wav","Alexa-coin.wav"
	,"pizza-singleword.wav","coin-singleword.wav","news-singleword.wav","song-singleword.wav","rain-singleword.wav"]
	# phrase_list = ["Alexa, wake me up everyday at 9am", "Alexa, wake me up everyday at 9am"]
	# file_list = ["Alexa-9am-m.wav", "Alexa-9am.wav"]
	count = 0
	while count < len(phrase_list):

		# Converts the audio file into an readable input
		r = sr.Recognizer()
		dir = os.path.dirname(os.path.realpath(__file__))
		dir = os.path.join(dir,"SampleRecordings")
		audioFile = sr.AudioFile(os.path.join(dir,file_list[count]))
		with audioFile as source:
			#r.adjust_for_ambient_noise(source, duration=0.5)
			audio = r.record(source)



		# Alternative google transcriptions

		print("----------------------------------")
		print("Actual Phrase: " + phrase_list[count])
		try:
			google_text = r.recognize_google(audio, show_all=True)
			print(google_text)
			# for text in google_text['alternative']:
			# 	print(text['transcript'])
		except:
			print("no results")
		#print(google_text)
		



		# print("----------------------------------")
		# print("Actual Phrase:")
		# print(phrase_list[count])
		# sphinx_text = r.recognize_sphinx(audio)
		# try:
		# 	google_text = r.recognize_google(audio)
		# except:
		# 	google_text = "NULL" #Google api could not understand speech
		# #google_text = "null"
		# print("Sphinx transcription:")
		# print(re.sub(r'([^\s\w]|_)+', '', sphinx_text))
		# print("Google transcription:")
		# print(re.sub(r'([^\s\w]|_)+', '', google_text))
		# say(re.sub(r'([^\s\w]|_)+', '', sphinx_text)) 
		# say(re.sub(r'([^\s\w]|_)+', '', google_text))




		count+=1



if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()