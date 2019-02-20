#!/usr/bin/python3.4
#written by Kirk Hammond 20150710. kirkdhammond@gmail.com
#this scipt was developed and executed on Fedora 22. I have not tested any version of python other than 3.4

# script will locate all .mp3 files in a directory and convert them to .flac files.
#I wrote this after purchasing a car deck that will play flac files that had some issues with mp3 files showing up as n/a, but all flac files played fine.

#usage:
# ./mp3toflac.py <target_dir>


# Edited by Amy Baer. amyjbaer@gmail.com. Script now only converts one file at a time.
# new usage:
# python mp3toflac.py <target_file>


#import modules
import os
import sys
from subprocess import call

#convert mp3 to flac if the flac target file does not already exist
def convert_mp3(mp3_file):
        flac = mp3_file[:-4] + ".flac"
        if os.path.isfile(flac):
            print('File ' + flac + ' already exists')
        else:
            call(["ffmpeg", "-i", mp3_file, flac])


