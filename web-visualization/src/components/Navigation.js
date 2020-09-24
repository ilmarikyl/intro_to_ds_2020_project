import React from "react";
import { AppBar, Typography, Toolbar } from "@material-ui/core";

const Navigation = () => {
  return (
    <AppBar
      style={{
        alignItems: "center",
        marginBottom: "16px",
        backgroundColor: "#1d3557",
      }}
      position="static"
    >
      <Toolbar variant="dense">
        <Typography variant="h5" component="h1">
          Fuck 2020
        </Typography>
      </Toolbar>
    </AppBar>
  );
};

export default Navigation;
