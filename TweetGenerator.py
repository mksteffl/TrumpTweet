from random import choice

class TweetGenerator(object):

    def __init__(self, open_file):
        self.corpus = open_file.read()
        self.words = self.corpus.split()
        self.d = self.build_dict(self.words)

    def build_dict(self, words):
        """
        Build a dictionary from the words.
        (word1, word2) => [w1, w2, ...]  # key: tuple; value: list
        """
        d = {}
        for i, word in enumerate(words):
            try:
                first, second, third = words[i], words[i+1], words[i+2]
            except IndexError:
                break
            key = (first, second)
            if key not in d:
                d[key] = []

            d[key].append(third)

        return d

    #will generate a complete sentence, starting with a randomly selected word and
    #ending when it encounters a '.'/'?'/'!'
    def generate_tweet(self):
        EOS = ['.', '?', '!']
        li = [key for key in self.d.keys() if key[0][0].isupper()]
        key = choice(li)
        li = []
        first, second = key
        li.append(first)
        li.append(second)
        while True:
            try:
                third = choice(self.d[key])
            except KeyError:
                break
            li.append(third)
            if third[-1] in EOS:
                break
            # else
            key = (second, third)
            first, second = key

        return ' '.join(li)
