import React from "react";
import CalendarHeatmap from "react-calendar-heatmap";
import ReactTooltip from "react-tooltip";

const today = new Date();

const Calendar = ({ selectDate }) => {
  const getTooltip = (value) => {
    return { "data-tip": value.date };
  };

  function shiftDate(date, numDays) {
    const newDate = new Date(date);
    newDate.setDate(newDate.getDate() + numDays);
    return newDate;
  }

  function getRange(count) {
    return Array.from({ length: count }, (_, i) => i);
  }

  function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  const randomValues = getRange(300).map((index) => {
    return {
      date: shiftDate(today, -index),
      count: getRandomInt(0, 2),
    };
  });

  return (
    <>
      <CalendarHeatmap
        startDate={new Date("2019-12-31")}
        endDate={new Date("2020-06-01")}
        values={randomValues}
        classForValue={(value) => {
          if (!value) {
            return "color-empty";
          }
          return `color-scale-${value.count}`;
        }}
        showWeekdayLabels={true}
        gutterSize={2}
        onClick={selectDate}
        tooltipDataAttrs={getTooltip}
      />
      <ReactTooltip />
    </>
  );
};

export default Calendar;
