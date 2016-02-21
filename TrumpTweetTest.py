import TweetGenerator

file  = open("WindowsCorpus.txt", "rt")
tweetGen = TweetGenerator.TweetGenerator(file)

for i in range(0,10):
    sampleTweet = tweetGen.generate_tweet()
    print(sampleTweet)
