import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sents = ['positive', 'negative', 'neutral']
# sns.set(style='whitegrid', palette='muted', font_scale=1.2)
sns.set(style="white", context="talk")
plt.figure(figsize=[10,7])

# Read CSVs with predictions
df_trump = pd.read_csv('../model/tweet_predictions/trump_2020_tweets_predictions.csv', sep='\t')
df_biden = pd.read_csv('../model/tweet_predictions/biden_2020_tweets_predictions.csv', sep='\t')

# Drop rows where 'opponent_mentioned' == False
# df_trump_opp_mentioned = df_trump.drop(df_trump[df_trump.opponent_mentioned == False].index)
# df_biden_opp_mentioned = df_biden.drop(df_biden[df_biden.opponent_mentioned == False].index)

# Code below uses Seaborn to plot

# Trump
class_names = ['negative', 'neutral', 'positive']
ax = sns.countplot(df_trump.predicted_sent, order=['positive', 'negative', 'neutral'], palette=['#7BB662', '#E03C32', '#F5D22C'], saturation=1)
plt.xlabel('')
plt.title('Sentiment distribution of Trump\'s tweets')
for p in ax.patches:
    ax.annotate('{:d}'.format(p.get_height()), (p.get_x()+0.30, p.get_height()))
plt.show()
plt.clf()

# Biden
plt.figure(figsize=[10,7])
class_names = ['negative', 'neutral', 'positive']
ax = sns.countplot(df_biden.predicted_sent, order=['positive', 'negative', 'neutral'], palette=['#7BB662', '#E03C32', '#F5D22C'], saturation=1)
plt.title('Sentiment distribution of Biden\'s tweets')
for p in ax.patches:
    ax.annotate('{:d}'.format(p.get_height()), (p.get_x()+0.35, p.get_height()))
plt.xlabel('')
plt.show()
