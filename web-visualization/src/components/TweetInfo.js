import React from "react";
import Calendar from "./Calendar";
import { Paper, Grid, Typography } from "@material-ui/core";
import { Timeline } from "react-twitter-widgets";
import Tweets from "./Tweets";

const TweetInfo = ({ tweets, person, selectDate, selectedTweets }) => {
  if (!person) {
    return null;
  }

  return (
    <Paper style={{ backgroundColor: "#eddcd2", padding: "3em" }}>
      <Grid container spacing={2} style={{ paddingTop: "3em" }}>
        <Grid item xs={12} md={5}>
          <Typography variant="h5" gutterBottom>
            Tweet timeline
          </Typography>
          <Calendar selectDate={selectDate} tweets={tweets} />
        </Grid>
        <Grid item md={1}></Grid>
        <Grid item xs={12} md={6}>
          {!selectedTweets ? (
            <div>
              <Typography variant="h5" gutterBottom>
                Most recent tweets
              </Typography>
              <Timeline
                dataSource={{
                  sourceType: "profile",
                  screenName: person.username,
                }}
                options={{
                  height: "35em",
                }}
              />
            </div>
          ) : (
            <div>
              <Tweets tweets={selectedTweets} selectDate={selectDate} />
            </div>
          )}
        </Grid>
      </Grid>
    </Paper>
  );
};

export default TweetInfo;
