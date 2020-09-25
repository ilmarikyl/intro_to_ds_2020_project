import React from "react";
import Calendar from "./Calendar";
import { Paper, Grid, Typography } from "@material-ui/core";
import { Timeline } from "react-twitter-widgets";

const TweetInfo = () => {
  // const [selected, setSelected] = useState(null);

  const selectDate = (value) => {
    console.log("value", value);
    // setSelected(value.date);
  };
  return (
    <Paper style={{ backgroundColor: "#eddcd2", padding: "3em" }}>
      <Grid container spacing={2} style={{ paddingTop: "3em" }}>
        <Grid item xs={12} md={6}>
          <Typography variant="h5" gutterBottom>
            Tweet timeline
          </Typography>
          <Calendar selectDate={selectDate} />
        </Grid>
        <Grid item md={1}></Grid>
        <Grid item xs={12} md={5}>
          <Typography variant="h5" gutterBottom>
            Summary of a day
          </Typography>
          {/* <Paper style={{ backgroundColor: "#f0efeb", height: "100%" }}>
            <Typography variant="body1" style={{ fontWeight: 400 }}>
              More info here ...
            </Typography>
          </Paper> */}
          <Timeline
            dataSource={{
              sourceType: "profile",
              screenName: "realdonaldtrump",
            }}
            options={{
              height: "400",
            }}
          />
        </Grid>
      </Grid>
    </Paper>
  );
};

export default TweetInfo;
