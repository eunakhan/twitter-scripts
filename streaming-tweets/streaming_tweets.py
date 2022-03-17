#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv
from csv import DictWriter
import json
from urllib3.exceptions import ProtocolError


consumer_key=''
consumer_secret=''
access_key=''
access_secret=''

phrase = 'MeToo'

class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)
        tweet = json.dumps(tweet)
        print(tweet)
        with open('test_streaming_'+phrase+'.txt', 'a') as f:
            f.write(tweet+'\n')
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    try:
        #This handles Twitter authetification and the connection to Twitter Streaming API
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        stream = Stream(auth, l)
        stream.filter(track=[phrase])

    except(ProtocolError, AttributeError):
        pass


