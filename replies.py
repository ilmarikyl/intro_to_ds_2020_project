import tweepy
import csv

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '41787763-2F9OcnzGhNjYGc7jQz35B2nw6tmhMJRTBMSG5H6hY'
ACCESS_SECRET = 'uWkU6JgIx7OFAtlj9NgIzFPiUU4gzl8mZE1qSevPz6Cyx'
CONSUMER_KEY = 'FQK43tEhOaQKAEGbBnrWGRMHz'
CONSUMER_SECRET = 'DW21NFTBFfGfSt4hjHaJ0r9lNYG9TimI4sPdxzc18F2qtUwx4g'

# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

# Create API object
api = connect_to_twitter_OAuth()

firstTweet = api.user_timeline("@MariaOhisalo")[0]
print(firstTweet.text)
id = firstTweet.id
print("Tweet ID", id)

# Get user
user = api.get_user("MariaOhisalo")
user_name = 'MariaOhisalo'
# Set tweet id 
tweet_id = '1312451483737092099'

# Create a list for all replies to a tweet
replies=[]

with open("tweet_replies.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for tweet in tweepy.Cursor(api.search,q='to:'+user_name, result_type='recent', timeout=999999).items(1000):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==tweet_id):
                replies.append(tweet)
                reply_text = tweet.text
                # Write reply to csv
                writer.writerow([reply_text])
                # print(reply_text)

