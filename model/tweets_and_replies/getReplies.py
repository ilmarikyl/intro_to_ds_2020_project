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

# Get user
user_name = 'MariaOhisalo'

# Get tweet
firstTweet = api.user_timeline("@MariaOhisalo")[3]
#firstTweet = api.user_timeline("@JoeBiden")[0]

# Set tweet id 
tweet_id = firstTweet.id
#tweet_id = '1313319274677768193' # biden 6.10.

replies = []

with open("tweet_replies_most_pos_biden.csv", "w", newline="") as file:
    writer = csv.writer(file)
    while (len(replies) <= 100):
        for tweet in tweepy.Cursor(api.search,q='to:'+user_name, result_type='recent', tweet_mode="extended", timeout=999999).items(100): # original 1000
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                if (tweet.in_reply_to_status_id_str==tweet_id):
                    replies.append(tweet)
                    # print reply text
                    print(tweet.text)
                    print(tweet.full_text)
                    print(tweet.id)
                    #status = api.get_status(reply_id, tweet_mode="extended")
                    #print(status.full_text)
                    #replies.append(tweet)
                    #reply_text = tweet.text
                    # Write reply to csv
                    #writer.writerow([reply_text])
                    #print(reply_text)
