import React from "react";
import { styled } from "@material-ui/core/styles";
import { Paper, Typography } from "@material-ui/core";
import { Tweet } from "react-twitter-widgets";
import DaySummary from "./DaySummary";

const chooseColor = (sentiment) => {
  switch (sentiment) {
    case "positive":
      return "#7bb662";
    case "neutral":
      return "#f5d22c";
    case "negative":
      return "#e03c32";
    default:
      return "#A9A9A9";
  }
};

const chooseBackground = (sentiment) => {
  switch (sentiment) {
    case "positive":
      return "#b7dba7";
    case "neutral":
      return "#ffe775";
    case "negative":
      return "#e6625a";
    default:
      return "#C0C0C0";
  }
};

const SentimentBar = styled(({ sentiment, ...other }) => <div {...other} />)({
  backgroundColor: (props) => chooseColor(props.sentiment),
  textAlign: "center",
  padding: "1em 0 1em 0",
  boxShadow:
    "0px 2px 4px -1px rgba(0,0,0,0.2), 0px 4px 5px 0px rgba(0,0,0,0.14), 0px 1px 10px 0px rgba(0,0,0,0.12)",
});

const TweetContainer = styled(({ sentiment, ...other }) => (
  <Paper {...other} />
))({
  margin: "0em 0 3em 0",
  padding: "1em 0 1em 0",
  borderRadius: "0px",
  borderBottom: "1px solid gray",
  borderTop: "1px solid gray",
  backgroundColor: (props) => chooseBackground(props.sentiment),
});

const Tweets = ({ tweets, selectDate }) => {
  return (
    <>
      <DaySummary
        tweets={tweets}
        chooseColor={chooseColor}
        selectDate={selectDate}
      />
      <div className="scrollable-container">
        <div id="scrollable">
          {tweets.map((tweet) => (
            <TweetContainer
              className="tweet"
              sentiment={tweet.predicted_sent}
              key={tweet.id}
              elevation={0}
            >
              <SentimentBar sentiment={tweet.predicted_sent} position="static">
                <Typography variant="subtitle1" style={{ fontWeight: "400" }}>
                  {tweet.predicted_sent.toUpperCase()}
                </Typography>
                {tweet.opponent_mentioned && (
                  <Typography variant="subtitle2" style={{ fontWeight: "400" }}>
                    Opponent mentioned
                  </Typography>
                )}
              </SentimentBar>
              <Tweet tweetId={tweet.id} />
            </TweetContainer>
          ))}
        </div>
      </div>
    </>
  );
};

export default Tweets;
