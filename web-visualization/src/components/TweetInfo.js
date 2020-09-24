import React from "react";
import Calendar from "./Calendar";
import { Paper, Grid, Typography } from "@material-ui/core";

const TweetInfo = () => {
  // const [selected, setSelected] = useState(null);

  const selectDate = (value) => {
    console.log("value", value);
    // setSelected(value.date);
  };
  return (
    <Paper style={{ backgroundColor: "#eddcd2", padding: "3em" }}>
      <Typography variant="h5">Tweet analysis</Typography>
      <Grid container spacing={2} style={{ paddingTop: "3em" }}>
        <Grid item xs={12} md={6}>
          <Calendar selectDate={selectDate} />
        </Grid>
        <Grid item xs={0} md={1}></Grid>
        <Grid item xs={12} md={5}>
          <Paper style={{ backgroundColor: "#f0efeb", height: "100%" }}>
            <Typography variant="h6" style={{ fontWeight: 400 }}>
              More info
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </Paper>
  );
};

export default TweetInfo;
