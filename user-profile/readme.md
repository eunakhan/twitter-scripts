## Description
A script to collect user's profile features given their screenname.

## Instructions to run:
- Required packages: tweepy, pandas.
- Fill out the consumer key, consumer secret, access key, access secret for your twitter developer account before running the script.

### Input
A csv file containing only column of users' screenname for whom you want to collect the profile features (example input file included: users.csv).


### Output
Creates a csv file containing their profile features (example output file included: user_data2.csv), such as,
```verified, followers_count, friends_count, listed_count, favourites_count, statuses_count, created_at```. 

Note that all the features returned by the twitter API are not save here by the script. You can find the complete list returned by this API here: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user. 
