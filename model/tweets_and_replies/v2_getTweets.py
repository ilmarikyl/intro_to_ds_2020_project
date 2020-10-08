import csv, re, tweepy
import pandas as pd

# Variables that contains the credentials to access Twitter API

# TIILA
# ACCESS_TOKEN = '41787763-2F9OcnzGhNjYGc7jQz35B2nw6tmhMJRTBMSG5H6hY'
# ACCESS_SECRET = 'uWkU6JgIx7OFAtlj9NgIzFPiUU4gzl8mZE1qSevPz6Cyx'
# CONSUMER_KEY = 'FQK43tEhOaQKAEGbBnrWGRMHz'
# CONSUMER_SECRET = 'DW21NFTBFfGfSt4hjHaJ0r9lNYG9TimI4sPdxzc18F2qtUwx4g'

#OMA
ACCESS_TOKEN = '1066379221600296960-4HS0jke0RX11mGXlOnpO896C04Wxbd'
ACCESS_SECRET = 'OPMyyJ9AO8ubdbplMpGiSeqzrkY69MqrKWZbSM04OBMK4'
CONSUMER_KEY = 'gTBAriQdYykUhTWJ92Ez6V60b'
CONSUMER_SECRET = 's7qm1CFH3sIWGQ7wZbMeIZD8Kk4N1mA0zdAzWbGd0vebxQhbvE'

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

dates, ids, users, texts, opponent_was_mentioned= [], [], [], [], []

trump_nicknames = ["realdonaldtrump", "@realdonaldtrump", "donald", "trump", "president tweety"]
biden_nicknames = ["joebiden", "@joebiden", "joe", "biden", "sleepy joe", "sleepyjoe", "slow joe", "joe hiden", "o'biden"]

i = 0
# screen_name=usuario,count=None,since_id=None,max_id=None,trim_user=True,exclude_replies=True,contributor_details=False,include_entities=False).items(200)
# for tweet in tweepy.Cursor(api.user_timeline, id=user_name, timeout=9999999, tweet_mode='extended', count=None,since_id=None,max_id=None,exclude_replies=True,contributor_details=False,include_entities=False).items():

max_id_in_town = 1304192424462278200

for tweet in tweepy.Cursor(api.user_timeline, id=user_name, timeout=9999999, tweet_mode='extended').items():

	i +=1

	date_time = tweet.created_at
	date_time = date_time.strftime("%Y-%m-%d")
	tweet_text = re.sub('\n', ' ', tweet.full_text)
	tweet_text = re.sub('https://t.co/[a-zA-Z0-9]{10}', '', tweet_text)

	if "RT @" in tweet_text:
			continue

	opponent_mentioned = False

	for nickname in trump_nicknames:
		if nickname in tweet_text.lower():
			opponent_mentioned = True

	if opponent_mentioned:
		opponent_was_mentioned.append(True)
	else:
		opponent_was_mentioned.append(False)

	dates.append(date_time)
	ids.append(tweet.id_str)
	users.append(tweet.user.screen_name)
	texts.append(tweet_text)


	if i % 250 == 0:
		print(f'{i} tweets checked, saving file')

		tweet_dict = {"date": dates, "id": ids, "username": users, "text": texts, "opponent_mentioned": opponent_was_mentioned}
		df = pd.DataFrame(tweet_dict)
		df.to_csv('v2_biden_recent_tweets.csv', index=False, sep='\t')

	elif i % 50 == 0:
		print(f'{i} tweets checked')

	

tweet_dict = {"date": dates, "id": ids, "username": users, "text": texts, "opponent_mentioned": opponent_was_mentioned}

df = pd.DataFrame(tweet_dict)
df.to_csv('v2_biden_recent_tweets.csv', index=False, sep='\t')

print(f'\nChecked {i} tweets in total')
print(f'Wrote {len(texts)} tweets in csv')