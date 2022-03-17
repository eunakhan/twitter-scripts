## Description

This script uses twitter API to collect the people (id, name) who retweeted a particular tweet.

## Instructions to run
- Required packages: tweepy, pandas.
- Fill out the ```consumer key, consumer secret, access key, access secret``` for your twitter developer account before running the script.

## Input
This particular script takes in a csv file which has the 4th column as retweet count and 10th column as tweet id for which you want to collect the retweeters.

## Output
Adds twitter id and screenname (of retweeters) columns to the csv file.

Note: An example input (relevant2.csv) and output (with-retweet.csv) files are added.

Additional information about the retweet can also be collected. For example, if you want to get when this was retweeted, write,

```time = status._json['created_at']```
before line 36.

For more attribute, see here: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
