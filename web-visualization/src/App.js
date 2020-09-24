import React, { useEffect, useState } from "react";
import { Container, CssBaseline } from "@material-ui/core";
import "react-calendar-heatmap/dist/styles.css";
import "./App.css";
import Navigation from "./components/Navigation";
import Content from "./components/Content";
import { getUserInfo } from "./requests";

const App = () => {
  const [person, setPerson] = useState(null);

  useEffect(() => {
    const getPersonInfo = async () => {
      const user = await getUserInfo();
      setPerson(user.data[0]);
    };
    getPersonInfo();
  }, []);

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="lg">
        <Navigation />
        <Content person={person} />
      </Container>
    </React.Fragment>
  );
};

export default App;
