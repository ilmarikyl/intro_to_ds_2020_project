import React from "react";
import { Typography, Paper, Avatar, Grid } from "@material-ui/core";

const PersonInfo = ({ person }) => {
  console.log("person", person);

  return !person ? null : (
    <Paper style={{ backgroundColor: "#e63946", padding: "3em" }}>
      <Grid container>
        <Grid item xs={12}>
          <Avatar alt={person.name} src={person.profile_image_url} />
          <Typography variant="h5">{person.name}</Typography>
          <Typography variant="body2" gutterBottom>
            @{person.username}
          </Typography>
          <Typography variant="body1">{person.description}</Typography>
        </Grid>
      </Grid>
    </Paper>
  );
};

export default PersonInfo;
