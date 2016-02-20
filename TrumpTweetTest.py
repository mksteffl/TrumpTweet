import TweetGenerator

file  = open("text.txt", "rt")
tweetGen = TweetGenerator.TweetGenerator(file)

for i in range(0,6):
    sampleTweet = tweetGen.generate_sentence()
    print(sampleTweet)
