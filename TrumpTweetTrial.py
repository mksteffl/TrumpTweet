import TweetGenerator
import tweepy
import re

class TwitterAPI:
    def __init__(self):
        consumer_key = "bvDMrI3qCBR0wNVwcEbsRo2Rj"
        consumer_secret = "l6T4DqnGANlt8YhWT5Dzmd1peSHG6FR0vdroZ8xtyeWvo3MKyf"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "700867195497123841-gtN5yBfBYwZyG8Fyn9Jd06ajJQqJGGM"
        access_token_secret = "NLX7yXdhGELGhJ7VANyzE9RjkosdgCKm2Yi930lk2fJ3q"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

    def trends(self):
        print(self.api.trends_place(1))

    def timeline(self):
        public_tweets = self.api.user_timeline(id="realDonaldTrump")
        for tweet in public_tweets:
            string = tweet.text + ' '
            search = '(?<=\#)(.*?)(?=\ )'
            results = re.findall(search, string)
            for result in results:
                print(result)
            # result = re.search(search.decode('utf-8'), string.decode('utf-8'), re.I | re.U)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.timeline()
    file  = open("text.txt", "rt")
    tweetGen = TweetGenerator.TweetGenerator(file)
    twitter.tweet(tweetGen.generate_tweet())
