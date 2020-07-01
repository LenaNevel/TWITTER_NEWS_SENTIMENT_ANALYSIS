#importing the following
import tweepy
import pandas as pd
import numpy as np
import csv

## User Credentials
#set up access keys to the twitter API
#found in twitter developer created app
consumer_key = 'iaHEVN95ORackRWoNyr1Rgdyr'
consumer_secret = 'ROL2cvYr2DtHGmNp21UdZWUBKktFJ4oRjCQTyQLTsiN34J231f'
access_key = '1270776687647752193-5igh2q6rFjsJiUN12DnoiNHWFHPJSt'
access_secret = 'a6dO1W2hmGBRwrIIiMqW6ECQI1CpdhjNIneBwAAzhOCFq'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#liberal news
#tweet_mode : extracts the full text of the tweet. otherwise it's truncated
#count = max is 200
palmer_report = api.user_timeline(screen_name = 'PalmerReport', count = 200, tweet_mode='extended')
#conservative
breitbart_news = api.user_timeline(screen_name = 'BreitbartNews', count = 200, tweet_mode='extended')
#neutral
bloomberg = api.user_timeline(screen_name = 'Bloomberg', count = 200, tweet_mode='extended')

#Extracting the tweets from Palmer Report
palmer_report_tweets = []
for tweet in palmer_report:
    palmer = {}
    palmer['id'] = tweet.id
    palmer['author'] = 'PalmerReport'
    palmer['length'] = len(tweet.full_text)
    palmer['created_at'] = tweet.created_at
    palmer['like_count'] = tweet.favorite_count
    palmer['retweet_count'] = tweet.retweet_count
    palmer['full_text'] = tweet.full_text
    palmer['source'] = tweet.source

    palmer_report_tweets.append(palmer)

#saving the Palmer Report data in to a csv
palmer_df = pd.DataFrame(palmer_report_tweets)

palmer_df.to_csv('./data/palmer_report.csv', index = False)

#Extracting the tweets from Breitbart_news
breitbart = pd.DataFrame(data = [tweet.id for tweet in breitbart_news], columns = ['id'])
breitbart['author'] = 'BreitbartNews'
breitbart['length'] = np.array([len(tweet.full_text) for tweet in breitbart_news])
breitbart['created_at'] = np.array([tweet.created_at for tweet in breitbart_news])
breitbart['like_count'] = np.array([tweet.favorite_count for tweet in breitbart_news])
breitbart['retweet_count'] = np.array([tweet.retweet_count for tweet in breitbart_news])
breitbart['full_text'] = np.array([tweet.full_text for tweet in breitbart_news])
breitbart['source'] = np.array([tweet.source for tweet in breitbart_news])

breitbart.to_csv('./data/breitbart_news.csv', index = False)

#Extracting and saving bloomber tweets
header = ['id', 'author', 'length', 'created_at', 'like_count', 'retweet_count', 'full_text', 'source']
with open('./data/bloomberg.csv', 'w', newline = '') as f:
    writer = csv.writer(f, delimiter= ',')
    writer.writerow(header)


for tweet in bloomberg:
    bloomberg_tweets = []
    bloomberg_tweet = {}
    bloomberg_tweet['id'] = tweet.id
    bloomberg_tweet['author'] = 'Bloomberg'
    bloomberg_tweet['length'] = len(tweet.full_text)
    bloomberg_tweet['created_at'] = tweet.created_at
    bloomberg_tweet['like_count'] = tweet.favorite_count
    bloomberg_tweet['retweet_count'] = tweet.retweet_count
    bloomberg_tweet['full_text'] = tweet.full_text
    bloomberg_tweet['source'] = tweet.source

    bloomberg_tweets.append(bloomberg_tweet)
    bloomberg_df = pd.DataFrame(bloomberg_tweets)
    bloomberg_df.to_csv('./data/bloomberg.csv', mode = 'a', index = False, header = False)
