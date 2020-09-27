# API

import tweepy

#print(tweepy.__version__)

consumer_key="gJKTcVyku7l3p2ROdqtriK2AK"
consumer_secret="xJi7mj0sQFChtO1JaawxmAGoTUDoQZ2eJj040NIQ6aOw0vNkAp"
access_token="41787763-41787763-OZQqGyGlV21sqNYap840a9N37dSWxxdVEIvgVVhsX"
access_token_secret="CDLmHr3mlA59RG38Mi3hvm7tQpMZcIMUiomWEvpSrGZnc"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

userId = "ttiila"

#item = api.get_user(userId)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
