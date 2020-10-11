import tweepy
import csv

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

# Create API object
api = connect_to_twitter_OAuth()

# Define user
user_name = 'JoeBiden'

with open("recent_tweets_biden.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for tweet in tweepy.Cursor(api.user_timeline,id=user_name, timeout=999999).items(): 

        #hashtags = tweet.entities.hashtags
        #urls = tweet.entities.urls
        #user_mentions = tweet.entities.user_mentions
        #symbols = tweet.entities.symbols    
        date_time = tweet.created_at
        date_time = date_time.strftime("%m/%d/%Y, %H:%M:%S")        
        tweet_row = tweet.id_str, date_time, tweet.user.screen_name, tweet.text
        tweet_row = "".join(tweet_row)
        print(tweet_row)
        print(tweet.id, tweet.created_at, tweet.user.screen_name, tweet.text, tweet.in_reply_to_screen_name, tweet.is_quote_status, tweet.source, tweet.retweet_count, tweet.favorite_count)
        writer.writerow([tweet_row])
        
          
