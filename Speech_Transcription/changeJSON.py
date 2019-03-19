import sys
import csv
import argparse
import json



parser = argparse.ArgumentParser()
parser.add_argument('--audio_file', type=str, help='Input audio file. Must be gs path')

def main():

	args = parser.parse_args()
	audio_file = args.audio_file

	with open("brad_request_template.json") as file:
		data = json.load(file)

	data["audio"]["uri"] = str(audio_file)

	with open('brad_request_final.json', 'w') as outfile:
		json.dump(data, outfile)


if __name__ == '__main__':
    
    main()