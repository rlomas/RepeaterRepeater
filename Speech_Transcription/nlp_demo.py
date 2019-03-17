import spacy
import sys

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
