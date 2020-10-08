import csv, re, tweepy
import pandas as pd

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '41787763-2F9OcnzGhNjYGc7jQz35B2nw6tmhMJRTBMSG5H6hY'
ACCESS_SECRET = 'uWkU6JgIx7OFAtlj9NgIzFPiUU4gzl8mZE1qSevPz6Cyx'
CONSUMER_KEY = 'FQK43tEhOaQKAEGbBnrWGRMHz'
CONSUMER_SECRET = 'DW21NFTBFfGfSt4hjHaJ0r9lNYG9TimI4sPdxzc18F2qtUwx4g'

# Setup access to API
def connect_to_twitter_OAuth():
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	api = tweepy.API(auth, wait_on_rate_limit=True)
	return api

# Create API object
api = connect_to_twitter_OAuth()

# Define user
user_name = 'realDonaldTrump'

dates, ids, users, texts, opponent_was_mentioned= [], [], [], [], []

trump_nicknames = ["realdonaldtrump", "@realdonaldtrump", "donald", "trump", "president tweety"]
biden_nicknames = ["joebiden", "@joebiden", "joe", "biden", "sleepy joe", "sleepyjoe", "slow joe", "joe hiden", "o'biden"]

i = 0

for tweet in tweepy.Cursor(api.user_timeline, id=user_name, timeout=99999, tweet_mode='extended').items(500):

	#hashtags = tweet.entities.hashtags
	#urls = tweet.entities.urls
	#user_mentions = tweet.entities.user_mentions
	#symbols = tweet.entities.symbols

	date_time = tweet.created_at
	date_time = date_time.strftime("%Y-%m-%d")
	tweet_text = re.sub('\n', ' ', tweet.full_text)
	tweet_text = re.sub('https://t.co/[a-zA-Z0-9]{10}', '', tweet_text)

	if "RT @" in tweet_text:
			continue

	opponent_mentioned = False

	for nickname in biden_nicknames:
		if nickname in tweet_text.lower():
			opponent_mentioned = False

	if opponent_mentioned:
		opponent_was_mentioned.append(True)
	else:
		opponent_was_mentioned.append(False)

	dates.append(date_time)
	ids.append(tweet.id_str)
	users.append(tweet.user.screen_name)
	texts.append(tweet_text)

	i +=1


tweet_dict = {"date": dates, "id": ids, "username": users, "text": texts, "opponent_mentioned": opponent_was_mentioned}

df = pd.DataFrame(tweet_dict)
df.to_csv('v2_trump_recent_tweets.csv', index=False, sep='\t')

print(f'Checked {i} tweets')
print(f'Wrote {len(texts)} tweets in csv')