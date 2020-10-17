import React from "react";
import {
  Timeline,
  TimelineItem,
  TimelineSeparator,
  TimelineDot,
  TimelineConnector,
  TimelineContent,
} from "@material-ui/lab";
import { ButtonBase, Paper, Typography } from "@material-ui/core";
import events from "../data/events.json";

const EventTimeline = ({ selectDate }) => {
  return (
    <div className="calendar-container">
      <Timeline align="alternate">
        {events.map((event, i) => (
          <TimelineItem key={event.event}>
            <TimelineSeparator>
              <TimelineDot />
              {i !== events.length - 1 && <TimelineConnector />}
            </TimelineSeparator>
            <TimelineContent>
              <Typography style={{ padding: "0.5em" }}>{event.date}</Typography>
              <ButtonBase>
                <Paper
                  elevation={3}
                  className="event-item"
                  onClick={() => selectDate({ date: event.date })}
                >
                  <Typography align="left">{event.event}</Typography>
                </Paper>
              </ButtonBase>
            </TimelineContent>
          </TimelineItem>
        ))}
      </Timeline>
    </div>
  );
};

export default EventTimeline;
