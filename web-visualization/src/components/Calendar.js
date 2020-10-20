import React from "react";
import CalendarHeatmap from "react-calendar-heatmap";
import ReactTooltip from "react-tooltip";

const Calendar = ({ selectDate, tweets }) => {
  const getTooltip = (value) => {
    return { "data-tip": value.date };
  };

  return !tweets ? null : (
    <div className="calendar-container">
      <CalendarHeatmap
        startDate={new Date("2019-12-25")}
        endDate={new Date("2020-10-25")}
        values={tweets}
        classForValue={(value) => {
          if (!value) {
            return "color-empty";
          }
          return `color-scale-${value.color}`;
        }}
        showWeekdayLabels={true}
        showMonthLabels={true}
        gutterSize={2}
        onClick={selectDate}
        tooltipDataAttrs={getTooltip}
        horizontal={false}
      />
      <ReactTooltip />
    </div>
  );
};

export default Calendar;
