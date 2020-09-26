import pandas as pd
import preprocessor as pp

headers = ["date", "username", "to", "replies", "retweets",	"favorites", "text", "geo",	"mentions",	"hashtags", "id", "permalink"]

df = pd.read_csv("biden_personal.csv")
#print(df.head(5)) 

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


