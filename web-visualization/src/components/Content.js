import React from "react";
import { Grid } from "@material-ui/core";
import PersonInfo from "./PersonInfo";
import TweetInfo from "./TweetInfo";

const Content = ({ person }) => {
  return (
    <Grid container spacing={2}>
      <Grid item xs={12}>
        <PersonInfo person={person} />
      </Grid>
      <Grid item xs={12}>
        <TweetInfo />
      </Grid>
    </Grid>
  );
};

export default Content;
