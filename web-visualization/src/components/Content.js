import React from "react";
import { Grid } from "@material-ui/core";
import PersonInfo from "./PersonInfo";
import TweetInfo from "./TweetInfo";

const Content = ({
  person,
  tweets,
  togglePerson,
  selectDate,
  selectedTweets,
}) => {
  return (
    <Grid container spacing={2}>
      <Grid item xs={12}>
        <PersonInfo person={person} togglePerson={togglePerson} />
      </Grid>
      <Grid item xs={12}>
        <TweetInfo
          person={person}
          tweets={tweets}
          selectDate={selectDate}
          selectedTweets={selectedTweets}
        />
      </Grid>
    </Grid>
  );
};

export default Content;
