import json, re
import pandas as pd
from datetime import datetime


trump_nicknames = ["realdonaldtrump", "donald trump", "trump", "president tweety"]
biden_nicknames = ["joebiden", "joe biden", "biden", "sleepy joe", "sleepyjoe", "slow joe", "joe hiden", "o'biden"]

df = pd.read_csv('trump_2020_tweets_predictions.csv', sep='\t')
df = df.drop(['opponent_mentioned'], axis=1)

opponent_mentioned_list = []
was_mentioned = False

for tweet_text in df.text:
	for nickname in biden_nicknames:
			if nickname in tweet_text.lower():
				was_mentioned = True

	opponent_mentioned_list.append(was_mentioned)
	was_mentioned = False


df['opponent_mentioned'] = opponent_mentioned_list

df.to_csv('trump_2020_tweets_predictions_NEW.csv', index=False, sep='\t')
