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
        print self.api.trends_place(1)

    def timeline(self):
        public_tweets = self.api.user_timeline(id="OffensiveTweet_", count = 240)
        out_file = open("offensive.txt", "wt")
        for tweet in public_tweets:
            string = tweet.text.encode('utf8') + ' '
            string = re.sub('https:(.*?) ', '', string)
            string = re.sub('https:(.*?)\n', '', string)
            string = re.sub('&amp;', '', string)
            out_file.write(string + '\n')
        out_file.close()

if __name__ == "__main__":
    twitter = TwitterAPI()
    # twitter.trends();
    twitter.timeline();
    # twitter.tweet("My name is Mark and I love sucking HUGE veiny dicks")
