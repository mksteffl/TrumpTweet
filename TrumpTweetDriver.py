import TweetGenerator
import CorpusGenerator
import twitter

#scrape twitter and nyt, and add in with other trump texts
CorpusGenerator.CorpusGenerator()

#generate tweet using ngram/markov chain
tweet_maker = TweetGenerator.TweetGenerator("corpus.txt")
trump_tweet = tweet_maker.generate_tweet()

#tweet out the trump tweet
twitter = twitter.TwitterAPI()
twitter.tweet(trump_tweet)
