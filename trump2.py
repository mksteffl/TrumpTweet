import nltk
import sys
import re
import search_twitter
import context_free
import context_free_reader

part = dict()
words = list()
alltweets = list()
final = list()

query = {'q': 'therealdonaldtrump', 'rpp': 100} #max is 100

alltweets.append('hey baby lets fuck')
# for tweet in search_twitter.search_twitter(query):
# 	graphs = tweet['text'].encode('ascii', 'replace')
# 	alltweets.append(graphs)
for things in alltweets:
	things.strip(";:#-?.,")
	things.replace(".","")
	text = nltk.word_tokenize(things)
	tagged = nltk.pos_tag(text)
	for i in tagged:
		if re.search(r"\W",i[0]) or re.search(r"http",i[0]):
			pass
		else:
			if i[1] in part.keys():
				if i[0] in part.values():
					pass
				else:
					part[i[1]] += " | " + i[0]
			else:
				part[i[1]] = i[0]

for u in part.keys():
	thisone = u + " -> " + part[u]
	final.append(thisone)

last = "\n".join(final)

#Twitter
rules = "#clauses\nS -> I think NP VP SAID .\nS -> AS , I want to VB DT NP SAID .\nS -> I VBP NP AS SAID .\nNP -> DT JJ circus\nNP -> DT NN\nNP -> DT NNP\nVP -> VBN NP\nVP -> VBN\nDT VBG NN\nSAID ->, said NNP NNS \nAS -> as NNS VBN to VB\n#terminals\n"+last

file = open("rules3.txt", "w")
file.write(rules)
file.close()

cfree3 = context_free.ContextFree()

context_free_reader.add_rules_from_file(cfree3, open("rules3.txt"))
expansion3 = cfree3.get_expansion('S')
piece3 = ' '.join(expansion3)
piece3 = re.sub(r"\s\.",".",piece3)
piece3 = re.sub(r"\s,",",",piece3)
piece3 = re.sub(r"\s \s","\s",piece3)
piece3 = piece3.replace("  "," ")
piece3 = piece3.lower()
piece3 = piece3[0].upper() + piece3[1:]
quote = piece3.find(", said")
piece3 = "\"" + piece3[:quote+1] +  "\"" + piece3[quote+1:]

print piece3
