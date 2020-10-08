import numpy as np
import pandas as pd
from pylab import rcParams
import transformers, argparse, torch, sys
from transformers import BertModel, BertTokenizer, AdamW, get_linear_schedule_with_warmup
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from collections import defaultdict
from textwrap import wrap
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader

# Hyperparameters
RANDOM_SEED = 42
BATCH_SIZE = 16
MAX_LEN = 120
EPOCHS = 10

CLASS_NAMES = ['positive', 'negative', 'neutral']
PRE_TRAINED_MODEL_NAME = 'bert-base-cased'


class SentimentClassifier(nn.Module):

	def __init__(self, n_classes):
		super(SentimentClassifier, self).__init__()
		self.bert = BertModel.from_pretrained(PRE_TRAINED_MODEL_NAME)
		self.drop = nn.Dropout(p=0.3)
		self.out = nn.Linear(self.bert.config.hidden_size, n_classes)

	def forward(self, input_ids, attention_mask):
		_, pooled_output = self.bert(input_ids=input_ids, attention_mask=attention_mask)
		output = self.drop(pooled_output)

		return self.out(output)


class TweetDataset(Dataset):

	def __init__(self, tweets, targets, tokenizer, max_len):
		self.tweets = tweets
		self.targets = targets
		self.tokenizer = tokenizer
		self.max_len = max_len

	def __len__(self):
		return len(self.tweets)

	def __getitem__(self, item):
		tweet = str(self.tweets[item])
		target = self.targets[item]
		encoding = self.tokenizer.encode_plus(
			tweet,
			add_special_tokens=True,
			max_length=self.max_len,
			return_token_type_ids=False,
			pad_to_max_length=True,
			return_attention_mask=True,
			return_tensors='pt',
		)

		return {
			'tweet_text': tweet,
			'input_ids': encoding['input_ids'].flatten(),
			'attention_mask': encoding['attention_mask'].flatten(),
			'targets': torch.tensor(target, dtype=torch.long)
		}


def create_data_loader(df, tokenizer, max_len, batch_size):
	dataset = TweetDataset(
		tweets=df.tweet.to_numpy(),
		targets=df.sentiment.to_numpy(),
		tokenizer=tokenizer,
		max_len=max_len
	)

	return DataLoader(dataset, batch_size=batch_size, num_workers=4)


def train_epoch(model, data_loader, loss_fn, optimizer, device,	scheduler, n_examples):
	model = model.train()
	losses = []
	correct_predictions = 0

	for d in data_loader:
		input_ids = d["input_ids"].to(device)
		attention_mask = d["attention_mask"].to(device)
		targets = d["targets"].to(device)

		outputs = model(input_ids=input_ids, attention_mask=attention_mask)
		_, preds = torch.max(outputs, dim=1)
		loss = loss_fn(outputs, targets)
		correct_predictions += torch.sum(preds == targets)
		losses.append(loss.item())
		loss.backward()
		nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
		optimizer.step()
		scheduler.step()
		optimizer.zero_grad()

	return correct_predictions.double() / n_examples, np.mean(losses)

	
def evaluate_model(model, data_loader, loss_fn, device, n_examples):
	model = model.eval()
	losses = []
	correct_predictions = 0
	print('Evaluating model...')

	with torch.no_grad():
		for d in data_loader:
			input_ids = d["input_ids"].to(device)
			attention_mask = d["attention_mask"].to(device)
			targets = d["targets"].to(device)
			outputs = model(
				input_ids=input_ids,
				attention_mask=attention_mask
			)
			_, preds = torch.max(outputs, dim=1)
			loss = loss_fn(outputs, targets)
			correct_predictions += torch.sum(preds == targets)
			losses.append(loss.item())

	return correct_predictions.double() / n_examples, np.mean(losses)


def analyze_raw_text_line(tweet_text, tokenizer, model, device):
	encoded_tweet = tokenizer.encode_plus(tweet_text, max_length=MAX_LEN, add_special_tokens=True,	return_token_type_ids=False, pad_to_max_length=True, return_attention_mask=True, return_tensors='pt')
	input_ids = encoded_tweet['input_ids'].to(device)
	attention_mask = encoded_tweet['attention_mask'].to(device)
	output = model(input_ids, attention_mask)
	
	# print(output)
	scores = (round(output[0][0].item(), 3), round(output[0][1].item(), 3), round(output[0][2].item(), 3))

	return torch.max(output, dim=1), scores


def main(args):

	# Check if CUDA is available
	use_gpu = args.cuda and torch.cuda.is_available()
	device = torch.device("cuda:0") if use_gpu else "cpu"

	# Create tokenizer
	tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)

	# If argument is --predict_from_csv or -predict_from_input
	if args.predict_from_csv or args.predict_from_input:

		# Load model
		model = SentimentClassifier(len(CLASS_NAMES))
		model.load_state_dict(torch.load('model.bin', map_location=torch.device('cpu')))

		if args.predict_from_input:
			tweet_text = 'input'
			while tweet_text:
				tweet_text = input("Write/paste text here: ")
				(x, prediction), scores = analyze_raw_text_line(tweet_text, tokenizer, model, device)

				print(f'x: {x}, prediction: {prediction}, scores: {scores}')

				print(f'Text: {tweet_text}\nSentiment: {CLASS_NAMES[prediction]}\n')

		elif args.predict_from_csv:
			df = data = pd.read_csv(args.predict_from_csv, sep='\t', encoding='utf-8')
			# df = data = pd.read_csv(args.predict_from_csv, sep=',', encoding='utf-8') # for different delimiter
			output_filename = args.predict_from_csv.split('.')[0] + '_predictions.csv'
			top_sentiments =[]
			positives, negatives, neutrals = [], [], []
			
			print('Analyzing tweets...\n')
			for tweet_text in df['text']:
				if type(tweet_text) == str and len(tweet_text) > 1: # If tweet has no content, pandas tries to read next value on the row which is a float
					(x, prediction), scores = analyze_raw_text_line(str(tweet_text), tokenizer, model, device)
					positives.append(scores[0])
					negatives.append(scores[1])
					neutrals.append(scores[2])
					top_sentiments.append(CLASS_NAMES[prediction])
				else:
					top_sentiments.append('NO TEXT') # Tweet has no content
					positives.append('0') # No content = 0
					negatives.append('0')
					neutrals.append('0')

			df.insert(3, 'predicted_sent', top_sentiments, True)
			df.insert(3, 'neut_score', neutrals, True)
			df.insert(3, 'neg_score', negatives, True)
			df.insert(3, 'pos_score', positives, True)

			# Delete rows of which tweets don't have any text
			df = df.drop(df[df.predicted_sent == 'NO TEXT'].index)

			df.to_csv(output_filename, sep='\t', index=False)
			print(f'Done. Output file \'{output_filename}\' created.')

		exit(0)

	
	np.random.seed(RANDOM_SEED)
	torch.manual_seed(RANDOM_SEED)

	df = pd.read_csv("../annotated_tweets/tweet_data_numerical_classes.csv", sep='\t', header=None)
	df.columns = ['id', 'sentiment', 'tweet']

	# Create train and test sets
	df_train, df_test = train_test_split(df, test_size=0.1, random_state=RANDOM_SEED)
	df_val, df_test = train_test_split(df_test, test_size=0.5, random_state=RANDOM_SEED)

	# Create data loaders
	train_data_loader = create_data_loader(df_train, tokenizer, MAX_LEN, BATCH_SIZE)
	val_data_loader = create_data_loader(df_val, tokenizer, MAX_LEN, BATCH_SIZE)
	test_data_loader = create_data_loader(df_test, tokenizer, MAX_LEN, BATCH_SIZE)

	data = next(iter(train_data_loader))

	# If argument is --train
	if args.train:

		# Create new model
		model = SentimentClassifier(len(CLASS_NAMES))
		model = model.to(device)

		optimizer = AdamW(model.parameters(), lr=2e-5, correct_bias=False)
		total_steps = len(train_data_loader) * EPOCHS
		scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)
		loss_fn = nn.CrossEntropyLoss().to(device)

		input_ids = data['input_ids'].to(device)
		attention_mask = data['attention_mask'].to(device)

		# Train the model
		history = defaultdict(list)
		best_accuracy = 0
		for epoch in range(EPOCHS):
			print(f'Epoch {epoch + 1}/{EPOCHS}')
			print('-' * 10)
			train_acc, train_loss = train_epoch(
				model,
				train_data_loader,
				loss_fn,
				optimizer,
				device,
				scheduler,
				len(df_train)
			)
			print(f'Train loss: {train_loss}, Accuracy: {train_acc}')
			val_acc, val_loss = evaluate_model(model, val_data_loader, loss_fn,	device,	len(df_val))

			print(f'Validation loss: {val_loss}, Accuracy: {val_acc}')
			print()
			history['train_acc'].append(train_acc)
			history['train_loss'].append(train_loss)
			history['val_acc'].append(val_acc)
			history['val_loss'].append(val_loss)

			if val_acc > best_accuracy:
				# Save the model only if previous best validation accuracy is exceeded
				torch.save(model.state_dict(), 'model.bin')
				best_accuracy = val_acc

		print('\nFinished training the model.')

	# If argument is --evaluate
	if args.evaluate:
		
		# Load an existing model called 'model.bin' from script directory
		model = SentimentClassifier(len(CLASS_NAMES))
		model.load_state_dict(torch.load('model.bin', map_location=torch.device('cpu')))

		optimizer = AdamW(model.parameters(), lr=2e-5, correct_bias=False)
		total_steps = len(train_data_loader) * EPOCHS
		scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)
		loss_fn = nn.CrossEntropyLoss().to(device)

		test_acc, _ = evaluate_model(model,	test_data_loader, loss_fn, device, len(df_test))
		print(f'Accuracy on test set: {test_acc.item()}')


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Placeholder')
	parser.add_argument("--train", action="store_true", help="Train new model")
	parser.add_argument("--evaluate", action="store_true", help="Evaluate an existing model")
	parser.add_argument("--cuda", action="store_true", help="Use GPU")
	parser.add_argument("--predict_from_input", action="store_true", help="Write text to analyze")
	parser.add_argument("--predict_from_csv", type=str, help="Input a csv file with column called 'text'")

	args = parser.parse_args()

	if len(sys.argv) < 2:
		parser.print_usage()
		sys.exit(1)

	main(args)