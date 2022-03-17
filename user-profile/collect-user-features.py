import tweepy
import pandas as pd
import time 

  
# assign the values accordingly
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''


  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)

#----------
#------
udf = pd.read_csv("users.csv")
user_list = udf['user'].tolist()

print("user list length")
print(len(user_list))

collected_user=[]

verified=[]
followers_count=[]
friends_count=[]
listed_count=[]
favourites_count=[]
statuses_count=[]
created_at=[]

err=0
for user in user_list:
    print("fetching user: " + user)
    try:
        user_data = api.get_user(screen_name = user)
    except:
        print("got error.")
        err+=1
        print("error count: " + str(err))
        time.sleep(1)
        continue 
        
    collected_user.append(user)
    verified.append(user_data.verified)
    followers_count.append(user_data.followers_count)
    friends_count.append(user_data.friends_count)
    listed_count.append(user_data.listed_count)
    favourites_count.append(user_data.favourites_count)
    statuses_count.append(user_data.statuses_count)
    created_at.append(user_data.created_at)
    
    print("fetched user")

    time.sleep(1)

  
df = pd.DataFrame()
df['user']=collected_user
df['verified']=verified
df['followers_count']=followers_count
df['friends_count']=friends_count
df['listed_count']=listed_count
df['favourites_count']=favourites_count
df['statuses_count']=statuses_count
df['created_at']=created_at

df.to_csv("user_data2.csv", header=True, index=None)
