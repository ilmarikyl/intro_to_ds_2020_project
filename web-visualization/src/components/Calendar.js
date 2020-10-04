import React from "react";
import CalendarHeatmap from "react-calendar-heatmap";
import ReactTooltip from "react-tooltip";

const Calendar = ({ selectDate, tweets }) => {
  const getTooltip = (value) => {
    return { "data-tip": value.date };
  };

  return !tweets ? null : (
    <>
      <CalendarHeatmap
        startDate={new Date("2020-3-31")}
        endDate={new Date("2020-10-01")}
        values={tweets}
        classForValue={(value) => {
          if (!value) {
            return "color-empty";
          }
          return `color-scale-${value.color}`;
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
