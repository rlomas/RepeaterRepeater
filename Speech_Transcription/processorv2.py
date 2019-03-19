import spacy
import sys
import json
from collections import OrderedDict


# (1) Pull out all strings and scores from JSON file

filename = sys.argv[1]
with open(filename) as file:
    data = json.load(file)

if "error" in data.keys():
    print(data)
    exit(1)

google_results = OrderedDict()
for result in data["results"][0]["alternatives"]:
    confidence = -1
    if "confidence" in result.keys():
        confidence = result['confidence']
    google_results[result["transcript"]] = confidence

##########################################



# (2) Get score from POS analytics
def pos_analyze(transcript):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(transcript, 'utf-8')

    nouns = 0
    verbs = 0
    subject = 0

    # identifies parts of speech of each word
    for token in doc:
        if token.pos_ == u"VERB":
            verbs += 1
        if token.pos_ == u"NOUN":
            nouns += 1
        if 'subj' in token.dep_:
            subject += 1

    # TODO: come up with scoring system that's better
    score = 0
    if verbs > 0:
        score += 1
    if nouns > 0:
        score += 1
    if subject > 0:
        score += 1

    return score

pos_scores = OrderedDict()
for transcript in google_results.keys():
    pos_scores[transcript] = pos_analyze(transcript)

##########################################



# (3) Look at punctutation from google string
punctutation_scores = OrderedDict()
for transcript in google_results.keys():
    # TODO: Maybe add more points for questions, periods?
    punctutation_scores[transcript] = (transcript[-1] == '!' or transcript[-1] == '.' or transcript[-1] == '?')

##########################################

# TODO: should factor in the ordering of the google results (hence the orderedDict)


# (3) Cacluate final score and choose best option

##########################################



# (4) If debug flag, print out why option was chosen
if len(sys.argv) > 2 and (sys.argv[2] == '-d' or sys.argv[2] == '--debug'):
    for transcript in google_results.keys():
        print(transcript)
        print("\tTotal Score: ", "TODO")
        print("\tGoogle Confidence :", google_results[transcript])
        print("\tPOS Score: ", pos_scores[transcript])
        print("\tPunctuation Score: ", punctutation_scores[transcript])
        print("\tOrdering Adjustment: ", "TODO")
# (5) No debug flag, print our choice
else: 
    # TODO change this to actual choice
    print(google_results.keys()[0])

##########################################

