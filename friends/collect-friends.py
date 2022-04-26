__author__ = 'bhavtosh'

import tweepy

li = ['euna_khan'] # List of screen_names

consumer_key=''
consumer_secret=''
access_key=''
access_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
# api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5, retry_errors= set([401, 404, 500, 503]))


for i in range(len(li)):
    ids_frnd = []
    for page_fol in tweepy.Cursor(api.get_friend_ids, user_id=li[i], count=5000).pages():
        ids_frnd.extend(page_fol)
    
    print("Friends of " + li[i] + ":")
    print(ids_frnd)





