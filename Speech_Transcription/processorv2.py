# from spacy import load
import sys
import json
from collections import OrderedDict


# (1) Pull out all strings and scores from JSON file

mode = sys.argv[2]

filename = sys.argv[1]
with open(filename) as file:
    data = json.load(file)

if "error" in data.keys():
    print("There is an error, please try again")
    exit(1)

if "results" not in data.keys():
    print("No input found, please speak loudly and try again")
    exit(1)

google_results = OrderedDict()
for rank, result in enumerate(data["results"][0]["alternatives"]):
    google_results[result["transcript"]] = rank

##########################################


# (2) Get score from POS analytics
# def pos_analyze(transcript):
#     nlp = load('en_core_web_sm')
#     doc = nlp(transcript, 'utf-8')

#     nouns = 0
#     verbs = 0
#     subject = 0

#     # identifies parts of speech of each word
#     for token in doc:
#         if token.pos_ == u"VERB":
#             verbs += 1
#         if token.pos_ == u"NOUN":
#             nouns += 1
#         if 'subj' in token.dep_:
#             subject += 1

#     score = 0
#     if verbs > 0:
#         score += 1
#     if nouns > 0:
#         score += 1
#     if subject > 0:
#         score += 1

#     return score

# pos_scores = OrderedDict()
# for transcript in google_results.keys():
#     pos_scores[transcript] = pos_analyze(transcript)

##########################################


# (3) Look at punctutation from google string
punctutation_scores = OrderedDict()
for transcript in google_results.keys():
    # TODO: Maybe add more points for questions, periods?
    punctutation_scores[transcript] = (transcript[-1] == '!' or transcript[-1] == '.' or transcript[-1] == '?')

##########################################

# (4) check for shortcuts
for transcript in google_results.keys():
    if "time" in transcript.lower():
        print(mode + "What time is it? ")
        exit()
    elif "schedule" in transcript.lower():
        print(mode + "What my schedule is like today? ")
        exit()
    elif "joke" in transcript.lower():
        print(mode + "Tell me a joke.")
        exit()
    elif "messages" in transcript.lower():
        print(mode + "Read my messages.")
        exit()
    elif "date" in transcript.lower():
        print(mode + "What’s the date today? ")
        exit()
    elif "weather" in transcript.lower():
        print(mode + "What’s the weather today?")
        exit()
##########################################


# (3) Cacluate final score and choose best option
final_choice = ""
# highest_POS = (-1, "")
for transcript, rank in google_results.items():
    # if pos_scores[transcript] > highest_POS[0]:
    #     highest_POS = (pos_scores[transcript], transcript)
    if punctutation_scores[transcript]:
        final_choice = transcript
        break

if final_choice == "":
    final_choice = google_results.keys()[0]
# if google_results[final_choice] > google_results[highest_POS[1]] + 4:
#     final_choice = highest_POS[1]
##########################################


# (4) If debug flag, print out why option was chosen
if len(sys.argv) > 2 and (sys.argv[2] == '-d' or sys.argv[2] == '--debug'):
    for rank, transcript in enumerate(google_results.keys()):
        print(transcript)
        print("\tGoogle Ranking Order: ", rank)
        # print("\tPOS Score: ", pos_scores[transcript])
        print("\tPunctuation Score: ", punctutation_scores[transcript])
# (5) No debug flag, print our choice
else: 
    print(mode + final_choice)

##########################################

