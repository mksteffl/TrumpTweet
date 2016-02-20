import markovmaker

cantStumpHim = open("Small Sample.txt", "r")
markov = markovmaker.Markov(cantStumpHim)

for i in range(1,6):
    trumpTweet =  markov.generate_markov_text(3)
    #print(trumpTweet)

markov.trace_triples()

