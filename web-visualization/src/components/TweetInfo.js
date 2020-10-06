import React, { useState } from "react";
import Calendar from "./Calendar";
import { Paper, Grid, Typography } from "@material-ui/core";
import { Timeline, Tweet } from "react-twitter-widgets";

const TweetInfo = ({ tweets }) => {
  const [selectedTweets, setSelectedTweets] = useState(null);

  const selectDate = (value) => {
    const sameDateTweets = tweets.filter((t) => t.date === value.date);
    console.log("tviitit päivältä", sameDateTweets);
    const tweetIds = sameDateTweets.map((tweet) =>
      tweet.permalink.substring(tweet.permalink.lastIndexOf("/") + 1)
    );
    setSelectedTweets(tweetIds);
  };
  return (
    <Paper style={{ backgroundColor: "#eddcd2", padding: "3em" }}>
      <Grid container spacing={2} style={{ paddingTop: "3em" }}>
        <Grid item xs={12} md={6}>
          <Typography variant="h5" gutterBottom>
            Tweet timeline
          </Typography>
          <Calendar selectDate={selectDate} tweets={tweets} />
        </Grid>
        <Grid item md={1}></Grid>
        <Grid item xs={12} md={5}>
          {!selectedTweets ? (
            <div>
              <Typography variant="h5" gutterBottom>
                Latest tweets
              </Typography>
              <Timeline
                dataSource={{
                  sourceType: "profile",
                  screenName: "realdonaldtrump",
                }}
                options={{
                  height: "400",
                }}
              />
            </div>
          ) : (
            <div>
              <Typography variant="h5" gutterBottom>
                Tweets from selected date
              </Typography>
              <div id="scrollable">
                {selectedTweets.map((tweet) => (
                  <Tweet
                    key={tweet}
                    tweetId={tweet}
                    options={{ height: "200px" }}
                  />
                ))}
              </div>
            </div>
          )}
        </Grid>
      </Grid>
    </Paper>
  );
};

export default TweetInfo;
