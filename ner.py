#coding=utf-8
#Named Entity Recognizer
import nltk


text = """ President Obama on Monday will ban the federal provision of some
types of military-style equipment to local police departments and sharply
restrict the availability of others, administration officials said.
The ban is part of Mr. Obama's push to ease tensions between law
enforcement and minority communities in reaction to the crises in
Baltimore; Ferguson, Mo.; and other cities.
“There’s been too many incidents where he has made comments or members of his 
administration have made comments without knowing the facts,” Mr. Canterbury said. 
“He has certain views, and they’re drawn from his personal experiences and from
the advisers that he has around him, but it’s a skewed view.”
The strains surfaced late last year after the killing of a young black man by a 
white police officer in Ferguson, Mo., and again last month after the death of 
another black man who had been taken into police custody in Baltimore.
But they are nothing new for Mr. Obama, who came of age as a community organizer 
in Chicago, where the same toxic mix of poverty, racial tension and lack of 
opportunity often boiled over into hostility and violence. The president, 
who spent his childhood in Indonesia and Hawaii and attended elite schools, 
had a far different experience in his own youth, but he has talked about 
having felt racially profiled by the police as a young man.
From his earliest days in politics, as an Illinois state senator,
Mr. Obama tried to forge close connections with law enforcement. 
Back then, he pushed for legislation to require videotaped police 
interrogations and prohibit racial profiling, managing to win the 
backing of police organizations for his efforts. Now, as he has watched 
the tensions boiling over in cities around the country, advisers say he 
is determined to find a way to speak to the root causes without scapegoating the police.
“Right now, police around the country are under an enormous amount of 
scrutiny and pressure, so emotions run high,” Valerie Jarrett, a senior 
adviser to Mr. Obama, said in an interview.
“He has never put it all on the police,” she continued. 
“He’s responding because he appreciates the fact that law 
enforcement really does have the spotlight on them, so he 
doesn’t want to create the impression that they alone can 
solve some of these structural problems.” """

text = text.decode('utf-8')

text_sentences = nltk.sent_tokenize(text)

tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in text_sentences]

tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]




p = "PERSON"
person_list = []


'''
NOTE:
if p in text_part: branch is not correctly adding the 
tagged person entries to the person_list currently

'''

for x in tagged_sentences:
	text_part = str(nltk.ne_chunk(x))
	smart_find(text_part, p)
	#print text_part
	if p in text_part:
		person_list.append(text_part)
	
	#print nltk.ne_chunk(x)


print "People found in article:"
for y in person_list:
	print y
	