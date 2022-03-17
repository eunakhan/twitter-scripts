__author__ = 'bhavtosh'

import tweepy
import csv

acnt_id = ['alirezafathi'] # List of account usernames.

consumer_key=''
consumer_secret=''
access_key=''
access_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth) 
  
for acnt in acnt_id:
    with open('acnt2.txt', 'a') as f:
        writer = csv.writer(f)
        for status in tweepy.Cursor(api.user_timeline, screen_name=acnt).items():
            l = []
            l.append(status._json['id'])
            l.append(status._json['user']['id'])
            l.append(status._json['user']['friends_count'])
            l.append(status._json['user']['followers_count'])
            l.append(status._json['user']['favourites_count'])
            l.append(status._json['user']['listed_count'])
            l.append(status._json['user']['statuses_count'])
            l.append(status._json['user']['created_at'])
            l.append(status._json['retweet_count'])
            l.append(status._json['favorite_count'])
            l.append(status._json['created_at'])
            l.append(status._json['text'])
            print(status._json['id'])
            writer.writerow(l)

