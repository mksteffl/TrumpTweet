import TweetGenerator

file  = open("Cant Stump The Trump.txt", "rt")
tweetGen = TweetGenerator.TweetGenerator(file)

for i in range(0,10):
    sampleTweet = tweetGen.generate_tweet()
    print(sampleTweet)
