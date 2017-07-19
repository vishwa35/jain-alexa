from tokens import keys

import tweepy
from tweepy import OAuthHandler
from random import randint

consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']

auth = OAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

class RandomTweet:

  def get_tweet(handle):
      fifty_tweets = api.user_timeline(screen_name=handle, count=50)
      for tweet in fifty_tweets:
	      with open('quotes.txt', 'a+') as f:
	        f.write(tweet.text + "\n")


  if __name__ == '__main__':
      get_tweet("sadguruwhispers")
