import React from "react";
import { Typography, Paper, Avatar, Grid, Button } from "@material-ui/core";

const PersonInfo = ({ person, togglePerson }) => {
  return !person ? null : (
    <Paper
      className="segment"
      style={{
        backgroundColor:
          person.username === "realDonaldTrump" ? "#e63946" : "#2d75c5",
      }}
    >
      <Grid container>
        <Grid item xs={8}>
          <Avatar
            alt={person.name}
            src={person.profile_image_url.replace("_normal", "")}
            style={{ height: "6em", width: "6em", marginBottom: "1em" }}
          />
        </Grid>
        <Grid item xs={4} style={{ textAlign: "right" }}>
          <Button
            onClick={togglePerson}
            variant="contained"
            color={
              person.username === "realDonaldTrump" ? "primary" : "secondary"
            }
          >
            Change person
          </Button>
        </Grid>
        <Grid item xs={12} sm={6}>
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
