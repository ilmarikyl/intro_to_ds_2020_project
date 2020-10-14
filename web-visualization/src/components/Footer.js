import React from "react";
import { IconButton, Typography } from "@material-ui/core";
import GitHubIcon from "@material-ui/icons/GitHub";

const Footer = () => {
  return (
    <footer className="footer">
      <Typography
        variant="h6"
        align="center"
        color="textSecondary"
        gutterBottom
      >
        Project source
      </Typography>
      <div style={{ textAlign: "center" }}>
        <IconButton href="https://github.com/ilmarikyl/intro_to_ds_2020_project">
          <GitHubIcon />
        </IconButton>
      </div>
    </footer>
  );
};

export default Footer;
