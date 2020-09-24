import React from "react";
import { Container, CssBaseline } from "@material-ui/core";
import "react-calendar-heatmap/dist/styles.css";
import "./App.css";
import Navigation from "./components/Navigation";
import Content from "./components/Content";

const App = () => {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="md">
        <Navigation />
        <Content />
      </Container>
    </React.Fragment>
  );
};

export default App;
