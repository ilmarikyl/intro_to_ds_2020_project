import React, { useEffect, useState } from "react";
import { Container, CssBaseline } from "@material-ui/core";
import "react-calendar-heatmap/dist/styles.css";
import "./App.css";
import Navigation from "./components/Navigation";
import Content from "./components/Content";
import { getUserInfo } from "./requests";
import trumpData from "./data/trump_tweets.json";
import bidenData from "./data/biden_tweets.json";

const App = () => {
  const [trumpInfo, setTrumpInfo] = useState(null);
  const [bidenInfo, setBidenInfo] = useState(null);
  const [person, setPerson] = useState(null);
  const [trumpTweets, setTrumpTweets] = useState(null);
  const [bidenTweets, setBidenTweets] = useState(null);
  const [tweets, setTweets] = useState(null);
  const [selectedTweets, setSelectedTweets] = useState(null);

  const selectColor = (tweet, allTweets) => {
    const sameDate = allTweets.filter((t) => t.date === tweet.date);

    let neutScore = 0;
    let negScore = 0;
    let posScore = 0;
    for (let i = 0; i < sameDate.length; i++) {
      neutScore += sameDate[i].neut_score;
      negScore += sameDate[i].neg_score;
      posScore += sameDate[i].pos_score;
    }

    const maxScore = Math.max(neutScore, negScore, posScore);

    if (maxScore === posScore) {
      return "0";
    } else if (maxScore === neutScore) {
      return "1";
    } else if (maxScore === negScore) {
      return "2";
    }
  };

  useEffect(() => {
    const getPersonInfo = async () => {
      const res = await getUserInfo();
      setTrumpInfo(res.data[0]);
      setBidenInfo(res.data[1]);
      setPerson(res.data[0]);
    };

    const formatTweets = (data) => {
      const formattedTweets = data.map((tweet) => {
        return {
          ...tweet,
          color: selectColor(tweet, data),
        };
      });
      return formattedTweets;
    };

    getPersonInfo();
    setTrumpTweets(formatTweets(trumpData));
    setBidenTweets(formatTweets(bidenData));
    setTweets(formatTweets(trumpData));
  }, []);

  const togglePerson = () => {
    if (person.username === "realDonaldTrump") {
      setPerson(bidenInfo);
      setTweets(bidenTweets);
      if (selectedTweets) {
        setSelectedTweets(
          bidenTweets.filter((t) => t.date === selectedTweets[0].date)
        );
      }
    } else if (person.username === "JoeBiden") {
      setPerson(trumpInfo);
      setTweets(trumpTweets);
      if (selectedTweets) {
        setSelectedTweets(
          trumpTweets.filter((t) => t.date === selectedTweets[0].date)
        );
      }
    }
  };

  const selectDate = (value) => {
    if (!value) {
      return;
    }
    if (value === "back") {
      setSelectedTweets(null);
      return;
    }
    const sameDateTweets = tweets.filter((t) => t.date === value.date);
    setSelectedTweets(sameDateTweets);
  };

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="lg">
        <Navigation />
        <Content
          person={person}
          tweets={tweets}
          togglePerson={togglePerson}
          selectDate={selectDate}
          selectedTweets={selectedTweets}
        />
      </Container>
    </React.Fragment>
  );
};

export default App;
