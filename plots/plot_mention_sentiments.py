import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sents = ['positive', 'negative', 'neutral']
sns.set(style='whitegrid', palette='muted', font_scale=1.2)
sns.set(style="white", context="talk")
plt.figure(figsize=[10,7])

# Read CSVs with predictions
df_trump = pd.read_csv('../model/tweet_predictions/trump_2020_tweets_predictions.csv', sep='\t')
df_biden = pd.read_csv('../model/tweet_predictions/biden_2020_tweets_predictions.csv', sep='\t')

# Drop rows where 'opponent_mentioned' == False
df_trump_opp_mentioned = df_trump.drop(df_trump[df_trump.opponent_mentioned == False].index)
df_biden_opp_mentioned = df_biden.drop(df_biden[df_biden.opponent_mentioned == False].index)

# Code below uses Seaborn to plot

# Trump
class_names = ['negative', 'neutral', 'positive']
ax = sns.countplot(df_trump_opp_mentioned.predicted_sent, order=['positive', 'negative', 'neutral'], palette=['#7BB662', '#E03C32', '#F5D22C'], saturation=1)
plt.xlabel('')
plt.title('Sentiment distribution of Trump\'s tweets where Biden is mentioned')
for p in ax.patches:
    ax.annotate('{:d}'.format(p.get_height()), (p.get_x()+0.35, p.get_height()))
plt.show()
plt.clf()

# Biden
plt.figure(figsize=[10,7])
class_names = ['negative', 'neutral', 'positive']
ax = sns.countplot(df_biden_opp_mentioned.predicted_sent, order=['positive', 'negative', 'neutral'], palette=['#7BB662', '#E03C32', '#F5D22C'], saturation=1)
plt.title('Sentiment distribution of Biden\'s tweets where Trump is mentioned')
for p in ax.patches:
    ax.annotate('{:d}'.format(p.get_height()), (p.get_x()+0.35, p.get_height()))
plt.xlabel('')
plt.show()


# The commented code below uses Pandas's plotting tools. They don't look as nice.

# Get pos, neg, and neut counts
# df_trump_sent_counts = df_trump_opp_mentioned.groupby('predicted_sent').count().T
# trump_plot_df = pd.DataFrame([[df_trump_sent_counts.positive[0], df_trump_sent_counts.negative[0], df_trump_sent_counts.neutral[0]]])
# trump_plot_df.columns = sents

# df_biden_sent_counts = df_biden_opp_mentioned.groupby('predicted_sent').count().T
# biden_plot_df = pd.DataFrame([[df_biden_sent_counts.positive[0], df_biden_sent_counts.negative[0], df_biden_sent_counts.neutral[0]]])
# biden_plot_df.columns = sents

# Trump plot
# df = pd.DataFrame({'positive': trump_plot_df.positive, 'negative':trump_plot_df.negative, 'neutral':trump_plot_df.neutral})
# ax = df.plot.bar(
# 	title='Sentiment distribution for tweets where Biden is mentioned',
# 	stacked=False,
# 	width=1,
# 	color=['#7BB662', '#E03C32', '#F5D22C'],
# 	figsize=(9,6))
# ax1 = plt.axes()
# x_axis = ax1.axes.get_xaxis()
# x_axis.set_visible(False)
# ax.figure.savefig('trump_mentions_biden_sent_distr.jpg', format='jpeg', dpi=300)
# plt.clf()

# Biden plot
# df = pd.DataFrame({'positive': biden_plot_df.positive, 'negative':biden_plot_df.negative, 'neutral':biden_plot_df.neutral})
# ax = df.plot.bar(
# 	title='Sentiment distribution for tweets where Trump is mentioned',
# 	stacked=False,
# 	width=1,
# 	color=['#7BB662', '#E03C32', '#F5D22C'],
# 	figsize=(9,6))
# ax1 = plt.axes()
# x_axis = ax1.axes.get_xaxis()
# x_axis.set_visible(False)
# ax.figure.savefig('biden_mentions_trump_sent_distr.jpg', format='jpeg', dpi=300)