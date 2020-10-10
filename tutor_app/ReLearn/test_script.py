#to be deleted, testing NLP functions only and is not part of django 
#requires pip install spacy, python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Mark and John are sincere employees at Google. Joseph likes to go fishing. Wendy is very hardworking and kind. ')
noun_adj_pairs = []
for i,token in enumerate(doc):
    if token.pos_ not in ('NOUN','PROPN'):
        continue
    for j in range(i+1,len(doc)):
        if doc[j].pos_ == 'ADJ':
            noun_adj_pairs.append((token,doc[j]))
            break
print(noun_adj_pairs)


student = nlp("I am looking for a patient tutor")
t1 = nlp("I am a patient tutor")
t2 = nlp("I am a creative tutor")
t3 = nlp("I am an efficient tutor")

print(student.similarity(t1)) #output = 0.8102488775334881
print(student.similarity(t2)) #output = 0.786925031953063
print(student.similarity(t3)) #output = 0.7317013896252067