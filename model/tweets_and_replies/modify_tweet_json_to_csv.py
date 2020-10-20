import json, re
import pandas as pd
from datetime import datetime

with open('new_trump_2020_json.json', encoding='utf8') as json_file:
	tweets = json.load(json_file)

mon_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

dates, ids, users, texts, opponent_was_mentioned= [], [], [], [], []
trump_nicknames = ["realdonaldtrump", "@realdonaldtrump", "donald trump", "trump", "president tweety"]
biden_nicknames = ["joebiden", "@joebiden", "biden", "sleepy joe", "sleepyjoe", "slow joe", "joe hiden", "o'biden"]

for tweet in tweets:
	date_parts = tweet['created_at'].split()
	date_time = f'{date_parts[5]}-{mon_dict[date_parts[1]]}-{date_parts[2]}'

	opponent_mentioned = False

	tweet_text = tweet['text']
	tweet_text = re.sub('\n', ' ', tweet_text)
	tweet_text = re.sub('https://t.co/[a-zA-Z0-9]{10}', '', tweet_text)

	if "RT @" in tweet_text:
			continue

	for nickname in biden_nicknames:
		if nickname in tweet_text.lower():
			opponent_mentioned = True

	if opponent_mentioned:
		opponent_was_mentioned.append(True)
	else:
		opponent_was_mentioned.append(False)


	dates.append(date_time)
	ids.append(tweet['id_str'])
	users.append('RealDonaldTrump')
	texts.append(tweet_text)


tweet_dict = {"date": dates, "id": ids, "username": users, "text": texts, "opponent_mentioned": opponent_was_mentioned}

df = pd.DataFrame(tweet_dict)
df.to_csv('new_trump_2020_tweets.csv', index=False, sep='\t')