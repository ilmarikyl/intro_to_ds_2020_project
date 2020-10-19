import React from "react";
import { Typography, IconButton } from "@material-ui/core";
import { styled } from "@material-ui/core/styles";
import ArrowBackIcon from "@material-ui/icons/ArrowBack";

const DaySummary = ({ tweets, chooseColor, selectDate }) => {
  const createSummary = () => {
    console.log("twiitit", tweets);
    let pos = 0;
    let neut = 0;
    let neg = 0;
    let posScore = 0;
    let neutScore = 0;
    let negScore = 0;
    let mentions = 0;

    const overall =
      tweets[0].color === "0"
        ? "positive"
        : tweets[0].color === "1"
        ? "neutral"
        : "negative";

    for (let i = 0; i < tweets.length; i++) {
      posScore += tweets[i].pos_score;
      neutScore += tweets[i].neut_score;
      negScore += tweets[i].neg_score;

      if (tweets[i].opponent_mentioned) {
        mentions += 1;
      }

      if (tweets[i].predicted_sent === "positive") {
        pos += 1;
      } else if (tweets[i].predicted_sent === "neutral") {
        neut += 1;
      } else if (tweets[i].predicted_sent === "negative") {
        neg += 1;
      }
    }
    return {
      pos,
      neut,
      neg,
      posScore,
      neutScore,
      negScore,
      amount: tweets.length,
      overall,
      mentions,
    };
  };

  const OverallSentiment = styled(({ sentiment, ...other }) => (
    <div {...other} />
  ))({
    backgroundColor: (props) => chooseColor(props.sentiment),
    textAlign: "center",
    position: "relative",
    padding: "1em 0 1em 0",
    borderRadius: "0.5em 0.5em 0 0",
  });

  const information = createSummary();
  return (
    <OverallSentiment sentiment={information.overall}>
      <IconButton
        aria-label="back"
        onClick={() => selectDate("back")}
        style={{ position: "absolute", top: "0", left: "0" }}
      >
        <ArrowBackIcon />
      </IconButton>
      <Typography variant="h6" style={{ fontWeight: "400" }}>
        {information.overall.toUpperCase()}
      </Typography>
      <Typography variant="subtitle1" style={{ fontWeight: "300" }}>
        {information.pos} positive, {information.neut} neutral,{" "}
        {information.neg} negative
      </Typography>
      <Typography variant="subtitle1" style={{ fontWeight: "300" }}>
        Opponent mentioned {information.mentions} times
      </Typography>
    </OverallSentiment>
  );
};

export default DaySummary;
