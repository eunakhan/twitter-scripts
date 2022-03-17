import tweepy
import re
import csv
import pandas

consumer_key=''
consumer_secret=''
access_key=''
access_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

with open('relevant2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    mylist1=list(csv_reader)
    del mylist1[0]

newlist=[]

for row in mylist1:   

    newrow=row
    retweet_count=int(row[3])

    if retweet_count==0:
        newrow.append('-')
        newrow.append('-')

    else: #collect retweets
        t_id=int(row[9]) #tweet id 
        ids=''
        names=''
        for status in api.retweets(t_id, 100):
            retweeter_id=status._json['user']['id']
            thisid=str(retweeter_id)
            ids=ids+thisid
            ids=ids+' '

            retweeter_name=status._json['user']['screen_name']
            names=names+retweeter_name
            names=names+' '


        newrow.append(ids)
        newrow.append(names)
    newlist.append(newrow)

with open('with-retweet.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['username', 'user_id', 'date', 'retweets', 'favorites', 'text', 'geo', 'mentions', 'hashtags', 'id', 'permalink', 'retweeter_ids', 'retweeter_names'])
    writer.writerows(newlist)   
