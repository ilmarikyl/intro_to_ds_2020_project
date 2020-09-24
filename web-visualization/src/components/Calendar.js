import React from "react";
import CalendarHeatmap from "react-calendar-heatmap";

const Calendar = () => {
  return (
    <CalendarHeatmap
      startDate={new Date("2019-12-31")}
      endDate={new Date("2020-04-01")}
      values={[
        { date: "2020-01-02", count: 0 },
        { date: "2020-01-22", count: 1 },
        { date: "2020-03-22", count: 2 },
      ]}
      classForValue={(value) => {
        if (!value) {
          return "color-empty";
        }
        return `color-scale-${value.count}`;
      }}
      showWeekdayLabels={true}
    />
  );
};

export default Calendar;
