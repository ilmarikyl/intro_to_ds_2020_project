import React, { useState } from "react";
import Calendar from "./Calendar";
import { Paper, Grid, Typography } from "@material-ui/core";
import { ToggleButtonGroup, ToggleButton } from "@material-ui/lab";
import Tweets from "./Tweets";
import { Timeline } from "react-twitter-widgets";
import EventTimeline from "./EventTimeline";

const TweetInfo = ({ tweets, person, selectDate, selectedTweets }) => {
  const [view, setView] = useState("sentiment");

  const handleViewChange = (event, newView) => {
    if (newView) {
      setView(newView);
    }
  };

  if (!person) {
    return null;
  }

  return (
    <Paper className="segment" style={{ backgroundColor: "#eddcd2" }}>
      <Grid container spacing={2} style={{ paddingTop: "3em" }}>
        <Grid item xs={12} sm={5} style={{ marginBottom: "3em" }}>
          <div style={{ textAlign: "center", marginBottom: "1.5em" }}>
            <ToggleButtonGroup
              value={view}
              exclusive
              onChange={handleViewChange}
              aria-label="button group for timeline"
            >
              <ToggleButton value="sentiment">sentiment</ToggleButton>
              <ToggleButton value="event">events</ToggleButton>
            </ToggleButtonGroup>
          </div>
          {view === "sentiment" ? (
            <Calendar selectDate={selectDate} tweets={tweets} />
          ) : (
            <EventTimeline selectDate={selectDate} />
          )}
        </Grid>
        <Grid item sm={1}></Grid>
        <Grid item xs={12} sm={6}>
          {!selectedTweets ? (
            <div>
              <Typography variant="h5" style={{ marginBottom: "1.5em" }}>
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
