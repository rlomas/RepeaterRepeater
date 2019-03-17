import spacy
import sys

# (1) Pull out all strings and scores from JSON file

    # if no score is given, bypass this step

##########################################



# (2) Get score from POS analytics
input = sys.argv[1].decode('utf-8')
nlp = spacy.load('en_core_web_sm')

doc = nlp(input)

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

print("Nouns " + str(nouns))
print("Verbs " + str(verbs))
print("Subjects " + str(subject))
##########################################



# (3) Look at punctutation from google string

##########################################



# (3) Cacluate final score and choose best option

##########################################



# (4) If debug flag, print out why option was chosen

##########################################

