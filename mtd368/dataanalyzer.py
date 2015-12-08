"""The dataanalyzer module handles the majority of data analysis and summarization of
statistics for user analysis."""

#author: Matthew Dunn
#netID: mtd368
#date: 12/12/2015

import os
import numpy as np
import pandas as pd
from datemanager import numberOfDaysinStartMonth

class snowAnalyzer (object):
    def __init__ (self, weather, weekstartdate, weekenddate, deviationpenalty):
        self.weekstartdate = weekstartdate
        self.weekenddate = weekenddate
        self.weather = weather
        self.deviationpenalty = deviationpenalty

    def skiScorer(self):
        groupedByMean = self.weeklySummaryMetrics()
        groupedByMean = groupedByMean*0.0393701 # convert from millimeters to inches
        groupedByMean['AverageScore'] = groupedByMean['mean']/groupedByMean['std']
        groupedByMean['AverageScore2'] = (groupedByMean['mean']/(groupedByMean['std']*self.deviationpenalty))
        groupedByMean.sort_values('AverageScore2', ascending=False, inplace=True) # This is where I can sort by skiet type.
        print groupedByMean.head()
        return groupedByMean.head()

    def weeklySummaryMetrics(self):
        summaryWeeklyMetricsCalculated = self.weeklyMetrics()
        columnValuesDays = list(summaryWeeklyMetricsCalculated.columns.get_level_values(1))
        sortpivt = summaryWeeklyMetricsCalculated.loc[:,('mean',columnValuesDays[:8])]
        summaryWeekMetricsTransposed = summaryWeeklyMetricsCalculated.T
        groupbysummean = summaryWeekMetricsTransposed.groupby(level=0).mean().dropna()
        groupbysummean = groupbysummean.T
        return groupbysummean

    def weeklyMetrics(self):
        weeklyMetricsCalculated = self.builddataframeforgivenweeks()
        weeklyMetricsCalculated['StationsTemp'] = weeklyMetricsCalculated.index
        stationSplit = weeklyMetricsCalculated['StationsTemp']
        onlyStations = stationSplit.str[:-4]
        weeklyMetricsCalculated['Station'] = onlyStations
        weeklyMetricsCalculated.drop('StationsTemp',axis=1,inplace=True)
        pivt = weeklyMetricsCalculated.pivot_table(index=['Station'],aggfunc=[np.mean,np.std,np.max])
        return pivt

    def builddataframeforgivenweeks (self):
        if self.datesofweekinsamemonthchecker(self.weekstartdate, self.weekenddate) == 1:
            skiPeriodData = self.skiPeriodSplitter(self.weekstartdate.month, self.weekstartdate.day, self.weekenddate.day)
            return skiPeriodData
        else:
            numberofdaysinstartmonth, startMonthLastDay = numberOfDaysinStartMonth(self.weekstartdate) # send dates to weeksacrossmonthsmanager to get the exact day intervals for each month
            dateOfStartDay = startMonthLastDay - numberofdaysinstartmonth
            return self.skiPeriodMerger(startMonthLastDay)

    def skiPeriodMerger (self, startEndDate):
        startSkiPeriod = self.skiPeriodSplitter(self.weekstartdate.month, self.weekstartdate.day, startEndDate) #add startdate and enddate
        endSkiPeriod = self.skiPeriodSplitter(self.weekenddate.month, 01, self.weekenddate.day) #just add 01 and weekendate.day
        mergedSkiPeriod = pd.concat([startSkiPeriod, endSkiPeriod], axis=1)
        return mergedSkiPeriod

    def skiPeriodSplitter (self, month, startdate, enddate):
        monthTemp = int(month)
        weekofrawdata = self.weather.ix[self.weather.Month == monthTemp]
        startdatecolumnname = 'Day'+str(startdate).zfill(2)
        enddatecolumnname = 'Day'+str(enddate).zfill(2)
        precipitationforperiod = weekofrawdata.loc[:,startdatecolumnname:enddatecolumnname]
        return precipitationforperiod

    def datesofweekinsamemonthchecker(self, weekstartdate, weekenddate):
        startmonth = weekstartdate.month
        endmonth = weekenddate.month
        if startmonth == endmonth:
            return 1
        return 0
