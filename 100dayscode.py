#100daysofcode twitter bot by @rajneeshdangar



import tweepy
import time

consumer_key = ''  #enter consumer_key here
consumer_secret = '' #enter consumer_secret here
key = ''  #enter key here
secret = '' #enter secret here

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtags = '#100DaysOfCode'

tweetnumber = 1000  #Here you can add number of tweets yo want to retweets and like.

tweets = tweepy.Cursor(api.search_tweets,hashtags).items(tweetnumber)

def searchBot():
  for tweet in tweets:
    try:
        tweet.favourite()
        tweet.retweet()
        time.sleep(60)
        print('Retweet Ok ')


    except Exception as e:
      print(e)
      time.sleep(2)



searchBot()


#still if you find any query you can dm me on twitter at @rajneeshdangar, thank you.
