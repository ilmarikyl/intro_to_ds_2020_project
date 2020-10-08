import React, { useState } from "react";
import Calendar from "./Calendar";
import { Paper, Grid, Typography } from "@material-ui/core";
import { Timeline } from "react-twitter-widgets";
import Tweets from "./Tweets";

const TweetInfo = ({ tweets }) => {
  const [selectedTweets, setSelectedTweets] = useState(null);

  const selectDate = (value) => {
    const sameDateTweets = tweets.filter((t) => t.date === value.date);
    const sameDayFormatted = sameDateTweets.map((tweet) => {
      return {
        ...tweet,
        id: tweet.permalink.substring(tweet.permalink.lastIndexOf("/") + 1),
      };
    });
    console.log("same day", sameDayFormatted);
    setSelectedTweets(sameDayFormatted);
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
                  height: "600",
                }}
              />
            </div>
          ) : (
            <div>
              <Tweets tweets={selectedTweets} />
            </div>
          )}
        </Grid>
      </Grid>
    </Paper>
  );
};

export default TweetInfo;
