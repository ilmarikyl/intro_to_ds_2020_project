from wordcloud import WordCloud 
from collections import Counter
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt


def combine_preprocess_tweets(df):
	all_tweets_str = ''

	for tweet_text in df.text:
		no_punct_tweet_text = tokenizer.tokenize(tweet_text)
		filtered_lowered_tweet_text = [w.lower() for w in no_punct_tweet_text if not w.lower() in stop_words]
		final_tweet_text = ' '.join(filtered_lowered_tweet_text)
		all_tweets_str += f' {final_tweet_text}'
	
	tokens = nltk.word_tokenize(all_tweets_str)

	return nltk.FreqDist(tokens)


def generate_normal_wordcloud(freqs, outfile_name):
	wc = WordCloud(background_color='white', max_words=2500, width = 1920, height = 1080, stopwords=[])
	wc.generate_from_frequencies(freqs)
	wc.to_file(outfile_name)


def generate_wordcloud_with_mask(freqs, mask_img, outfile_name, format):
	mask = np.array(Image.open(mask_img))
	wc = WordCloud(background_color='white', mode='RGBA', max_words=500, mask=mask)
	wc.generate_from_frequencies(freqs)

	# Create coloring from image
	image_colors = ImageColorGenerator(mask)
	plt.figure(figsize=[16,16])
	plt.imshow(wc.recolor(color_func=image_colors), interpolation='bilinear')
	plt.axis('off')

	# Save to file
	plt.savefig(outfile_name, format=format, dpi=300)


def main():
	# Load dataframes
	df_trump = pd.read_csv('../model/tweet_predictions/trump_2020_tweets_predictions.csv', sep='\t')
	df_biden = pd.read_csv('../model/tweet_predictions/biden_2020_tweets_predictions.csv', sep='\t')

	# Create frequency lists
	trump_freqs = combine_preprocess_tweets(df_trump)
	biden_freqs = combine_preprocess_tweets(df_biden)

	# Trump wordclouds
	generate_normal_wordcloud(trump_freqs, 'wordcloud_trump_normal.png')
	generate_wordcloud_with_mask(trump_freqs, 'masks/rep_logo.png', 'wordcloud_trump_logo.png', 'png')

	# Biden wordclouds
	generate_normal_wordcloud(biden_freqs, 'wordcloud_biden_normal.png')
	generate_wordcloud_with_mask(biden_freqs, 'masks/dem_logo.png', 'wordcloud_biden_logo.png', 'png')


if __name__ == '__main__':
	# Create stop word list and tokenizer
	stop_words = nltk.corpus.stopwords.words('english')
	stop_words.append('amp')
	tokenizer = nltk.RegexpTokenizer(r'\w+')

	main()