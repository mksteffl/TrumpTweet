from collections import defaultdict
from random import random

class TweetGenerator(object):

    def __init__(self, corpus_file):
        self.titles = corpus_file.open().split('\n')
        self.markov_map = defaultdict(lambda:defaultdict(int))
        self.lookback = 2
        self.create_dict()

    def create_dict(self):
        #Generate map in the form word1 -> word2 -> occurences of word2 after word1
        for title in self.titles[:-1]:
            title = title.split()
            if len(title) > self.lookback:
                for i in range(len(title)+1):
                    self.markov_map[' '.join(title[max(0,i-self.lookback):i])][' '.join(title[i:i+1])] += 1

        #Convert map to the word1 -> word2 -> probability of word2 after word1
        for word, following in self.markov_map.items():
            total = float(sum(following.values()))
            for key in following:
                following[key] /= total

    #Typical sampling from a categorical distribution
    def sample(self, items):
        next_word = None
        t = 0.0
        for k, v in items:
            t += v
            if t and random() < v/t:
                next_word = k
        return next_word

    def generate_tweet(self):
        sentences = []
        while len(sentences) < 1:
            sentence = []
        next_word = self.sample(self.markov_map[''].items())
        while next_word != '':
            sentence.append(next_word)
            next_word = self.sample(self.markov_map[' '.join(sentence[-self.lookback:])].items())
        sentence = ' '.join(sentence)
        flag = True
        for title in self.titles: #Prune titles that are substrings of actual titles
            if sentence in title:
                print('Real tweet :(')
                flag = False
                break
        if len(sentence) > 140:
            print('Too long ;)')
            flag = False
        if flag:
            sentences.append(sentence)

        for sentence in sentences:
            return(sentence)






