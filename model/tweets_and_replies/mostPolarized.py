import pandas as pd

df = pd.read_csv("model/tweet_predictions/biden_personal_predictions.csv", sep="\t")
#/home/dell/Asiakirjat/IntroToDS2020/intro_to_ds_2020_project/model/tweet_predictions
print(df.head(5)) 

"""
>>> from urlparse import urlparse
>>> url = 'http://www.example.com/site/section1/VAR1/VAR2' 
>>> urlparse(url)
ParseResult(scheme='http', netloc='www.example.com', path='/site/section1/VAR1/VAR2', params='', query='', fragment='')
>>> urlparse(url).path
'/site/section1/VAR1/VAR2'
>>> urlparse(url).path.split('/')[-2]
'VAR1'
"""

cols = ["date", "username", "to", "replies", "retweets", "pos_score", "neg_score", "neut_score", "predicted_sent", "text", "mentions", "hashtags", "id", "permalink"]


#hae 15 positiivisinta ja 15 negatiivisinta ja printtaa niihin liittyen teksti + hastag

# niihin replyt + vie johkin csv jossa tiedot alkuperäsestä ja sit vastaukset? 

id = df["permalink"]
#id = id.apply(url.rsplit('/', 1)[-1])

# url.rsplit('/', 1)[-1]

most_pos = df.nlargest(100, "pos_score")
most_neg = df.nlargest(100, "neg_score")

print("Most POS: ", most_pos[["text", "to", "predicted_sent", "mentions", "hashtags"]])
print("Most POS: ", most_pos["permalink"])
print("Most NEG: ", most_neg[["text", "to", "predicted_sent", "mentions", "hashtags"]])

"""
df["text"] = df["text"].fillna("")

# pp.set_options(p.OPT.URL, p.OPT.EMOJI)
# All options:URLs, Hashtags, Mentions, Reserved words (RT, FAV), Emojis, Smileys

for i, row in df.iterrows():
    text = df["text"].values[i]
    cleaned = pp.clean(text)
    df["text"].values[i] = cleaned
 

df.to_csv("biden_personal_cleaned.csv", index=False)

df_cleaned = pd.read_csv("biden_personal_cleaned.csv")
#print(df_cleaned.head(5)) 


"""