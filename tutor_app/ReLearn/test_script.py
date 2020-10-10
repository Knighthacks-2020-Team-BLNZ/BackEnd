#to be deleted, testing NLP functions only and is not part of django 
#requires pip install spacy, python -m spacy download en_core_web_sm

import spacy
import pymysql

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='ReLearn2015',
                             db='Tutors')

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM entries"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()

nlp = spacy.load('en_core_web_md')
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


student = nlp("I am looking for a patient tutor. They should also be honest and direct.")
t1 = nlp("I am a patient tutor. I like to think I speak honestly and directly to my students.")
t2 = nlp("I am a creative tutor")
t3 = nlp("I am straightforward and transparent. I am an efficient tutor.")

print(student.similarity(t1)) 
print(student.similarity(t2)) 
print(student.similarity(t3)) 