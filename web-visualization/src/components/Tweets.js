import React from "react";
import { styled } from "@material-ui/core/styles";
import { Paper, Typography, AppBar, Toolbar } from "@material-ui/core";
import { Tweet } from "react-twitter-widgets";

const chooseColor = (sentiment) => {
  switch (sentiment) {
    case "positive":
      return "#7bb662";
    case "neutral":
      return "#f5d22c";
    default:
      return "#e03c32";
  }
};

const chooseBackground = (sentiment) => {
  switch (sentiment) {
    case "positive":
      return "#b7dba7";
    case "neutral":
      return "#ffe775";
    default:
      return "#e6625a";
  }
};

const SentimentBar = styled(({ sentiment, ...other }) => <AppBar {...other} />)(
  {
    backgroundColor: (props) => chooseColor(props.sentiment),
    alignItems: "center",
    borderRadius: "10px",
    color: "black",
  }
);

const TweetContainer = styled(({ sentiment, ...other }) => (
  <Paper {...other} />
))({
  margin: "0.5em 0 3em 0",
  padding: "1em 0 1em 0",
  borderBottom: "1px solid gray",
  backgroundColor: (props) => chooseBackground(props.sentiment),
});

const Tweets = ({ tweets }) => {
  return (
    <>
      <Typography variant="h5" gutterBottom>
        Tweets from {tweets[0].date}
      </Typography>
      <Paper elevation={0} style={{ padding: "2em 0 2em 0" }}>
        <div id="scrollable">
          {tweets.map((tweet) => (
            <TweetContainer
              sentiment={tweet.sentiment}
              key={tweet.id}
              elevation={0}
            >
              <SentimentBar sentiment={tweet.sentiment} position="static">
                <Toolbar>
                  <Typography>{tweet.sentiment}</Typography>
                </Toolbar>
              </SentimentBar>
              <Tweet tweetId={tweet.id} />
            </TweetContainer>
          ))}
        </div>
      </Paper>
    </>
  );
};

export default Tweets;
