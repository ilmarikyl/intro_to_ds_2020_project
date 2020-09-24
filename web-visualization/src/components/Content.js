import React from "react";
import Calendar from "./Calendar";
import { Typography, Paper, Grid } from "@material-ui/core";

const Content = () => {
  return (
    <Grid container spacing={1}>
      <Grid item xs={12}>
        <Paper>
          <Typography variant="h3" component="h2" gutterBottom>
            Donald Trump
          </Typography>
        </Paper>
      </Grid>
      <Grid item xs={12}>
        <Paper>
          <Grid container>
            <Grid item xs={6}>
              <Calendar />
            </Grid>
            <Typography>Infoa</Typography>
          </Grid>
        </Paper>
      </Grid>
    </Grid>
  );
};

export default Content;
