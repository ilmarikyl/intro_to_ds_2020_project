import { Paper, Typography, Grid } from "@material-ui/core";
import React from "react";
import bidenGraph from "../imgs/biden_sent_distr.svg";
import trumpGraph from "../imgs/trump_sent_distr.svg";
import bidenMentioned from "../imgs/biden_mentioned_sent_distr.svg";
import trumpMentioned from "../imgs/trump_mentioned_sent_distr.svg";
import bidenCloud from "../imgs/wordcloud_biden_logo.svg";
import trumpCloud from "../imgs/wordcloud_trump_logo.svg";

const Graphs = () => {
  return (
    <Paper className="segment">
      <Typography align="center" variant="h4" gutterBottom>
        Plots
      </Typography>
      <Grid container spacing={5}>
        <Grid item xs={12} sm={6}>
          <Typography align="center" variant="h5">
            Biden
          </Typography>
          <img
            src={bidenCloud}
            alt="Word cloud from biden's tweets"
            style={{ width: "100%" }}
          />
          <img
            src={bidenGraph}
            alt="sentiment distribution of biden's tweets"
            style={{ width: "100%" }}
          />
          <img
            src={trumpMentioned}
            alt="sentiment distribution of biden's tweets where trump is mentioned"
            style={{ width: "100%" }}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <Typography align="center" variant="h5">
            Trump
          </Typography>
          <img
            src={trumpCloud}
            alt="Word cloud from trump's tweets"
            style={{ width: "100%" }}
          />
          <img
            src={trumpGraph}
            alt="sentiment distribution of trump's tweets"
            style={{ width: "100%" }}
          />
          <img
            src={bidenMentioned}
            alt="sentiment distribution of trump's tweets where biden is mentioned"
            style={{ width: "100%" }}
          />
        </Grid>
      </Grid>
    </Paper>
  );
};

export default Graphs;
