import React, { useEffect, useState } from "react";
import { Container, CssBaseline } from "@material-ui/core";
import "react-calendar-heatmap/dist/styles.css";
import "./App.css";
import Navigation from "./components/Navigation";
import Content from "./components/Content";
import { getUserInfo } from "./requests";
import trumpData from "./data/trump_tweets.json";
// import bidenData from "./data/biden_tweets.json";

const App = () => {
  const [person, setPerson] = useState(null);
  const [tweets, setTweets] = useState(null);

  const formatDate = (date) => {
    return date.split(" ")[0];
  };

  //working but not a great solution for selecting calendar colours
  const selectColor = (tweet, allTweets) => {
    const sameDate = allTweets.filter((t) => t.date === tweet.date);

    let neut = 0;
    let neg = 0;
    let pos = 0;
    for (let i = 0; i < sameDate.length; i++) {
      if (sameDate[i].sentiment === "negative") {
        neg += 1;
      } else if (sameDate[i].sentiment === "postive") {
        pos += 1;
      } else if (sameDate[i].sentiment === "neutral") {
        neut += 1;
      }
    }

    const maxCount = Math.max(neut, neg, pos);
    return neut === maxCount ? 1 : neg === maxCount ? 2 : 0;
  };

  useEffect(() => {
    const getPersonInfo = async () => {
      const user = await getUserInfo();
      setPerson(user.data[0]);
    };

    const formatTweets = (data) => {
      const dateFormattedTweets = data.map((tweet) => {
        return {
          ...tweet,
          date: formatDate(tweet.date),
        };
      });
      const newTweets = dateFormattedTweets.map((tweet) => {
        return {
          ...tweet,
          color: selectColor(tweet, dateFormattedTweets),
        };
      });
      return newTweets;
    };

    getPersonInfo();
    setTweets(formatTweets(trumpData));
  }, []);

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="lg">
        <Navigation />
        <Content person={person} tweets={tweets} />
      </Container>
    </React.Fragment>
  );
};

export default App;
