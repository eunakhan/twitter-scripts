__author__ = 'bhavtosh'

import tweepy

li = ['euna_khan'] # List of screen_names

consumer_key=''
consumer_secret=''
access_key=''
access_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

for i in range(len(li)):
    ids_frnd = []
    for page_fol in tweepy.Cursor(api.friends_ids, user_id=li[i], count=5000).pages():
        ids_frnd.extend(page_fol)
    
    
print(ids_frnd)





