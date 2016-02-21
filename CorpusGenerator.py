#Generates the corpus which is used as the input for TweetGenerator.py
#Scrapes from the New York Times politcal top stories
#Scrapes Trumps most recent 240 tweets
#adds in transcripts from a bunch of other trump speeches

import json, requests
import re
import twitter

class CorpusGenerator(object):

    def __init__(self):
        self.out_file = open("corpus.txt", "wt")
        self.nyt_scrape()
        self.twitter_scrape()
        self.cobble_shit_together()
        self.out_file.close()

    def nyt_scrape(self):
        url = 'http://api.nytimes.com/svc/topstories/v1/politics.json?api-key=56ba07f49c4fe92ecb2624d7baab30ed:10:74482807'
        resp = requests.get(url=url)
        data = resp.json()
        results = data['results']
        for result in results:
            self.out_file.write(result['abstract'].encode('utf8') + '\n')

    def twitter_scrape(self):
        twitter_instance = twitter.TwitterAPI()
        tweets = twitter_instance.timeline()
        self.out_file.write(tweets)

    def cobble_shit_together(self):
        announce_file = open("Cant Stump The Trump.txt","rt")
        random_file = open("text.txt","rt")
        pres_announce = announce_file.read()
        random_shit = random_file.read()
        self.out_file.write(pres_announce)
        self.out_file.write(random_shit)

if __name__ == "__main__":
    CorpusGenerator()
