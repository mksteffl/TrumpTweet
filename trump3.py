import sys
import io
from pprint import pprint
from random import choice

EOS = ['.', '?', '!']


def build_dict(words):
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
        #
        d[key].append(third)

    return d

#will generate a complete sentence, starting with a randomly selected word and
#ending when it encounters a '.'/'?'/'!'
def generate_sentence(d):
    li = [key for key in d.keys() if key[0][0].isupper()]
    key = choice(li)

    li = []
    first, second = key
    li.append(first)
    li.append(second)
    while True:
        try:
            third = choice(d[key])
        except KeyError:
            break
        li.append(third)
        if third[-1] in EOS:
            break
        # else
        key = (second, third)
        first, second = key

    return ' '.join(li)


def main():
    with open("Cant Stump The Trump.txt", "rt") as f:
        text = f.read()

    words = text.split()
    d = build_dict(words)
    pprint(d)
    print()
    sent = generate_sentence(d)
    print(sent)
    if sent in text:
        print('# existing sentence :(')

####################

if __name__ == "__main__":
    main()
