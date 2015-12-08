"""This is a program that allows users to analyze the average snowfall by day across the
lower 48 states. The program uses NOAA data sets and allows the user to evaluate different
periods of the year to ski."""

#author: Matthew Dunn
#netID: mtd368
#date: 12/12/2015

import os
import sys
import re
import datetime
from datemanager import *
from dataloader import *
from dataanalyzer import *
from locationizer import *
from visualizer import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    try:
        # weathermeasurementtypefilebuilder() # this can be run each time or just once beacause it creates a text file with all the data for a specific precipitation type, currently set to SNOW.
        print "Loading Data..............."
        weathervaluesnorthamerica = monthlytextweatherdatamunger()
        # print weathervaluesnorthamerica.head()
        stations = staiondatamunger()
        # while unittype != "inch" or unittype != "cm":
        #     unittype = raw_input('What unit system would you like, metric(centimeters) or imperial(inches)? Please enter "inch" or "cm". \n')
        #     if unittype != "inch" or unittype != "cm":
        #         print 'Please enter "cm" or "inch". '
        while True:
            skidate = '2016-03-14'
            skidate2 = raw_input('When do you want to go SHRED the GNAR? MM-DD\n')
            deviationpenalty = raw_input('How much should we penalize the annual fluxations in average snowfall?\n')
            if skidate2 == 'quit':
                break
            # to do:
            ## ask what units they'd like to use
            ## ask if they want to risk big snow or likelyhood of snow
            try:
                possibleSkiWeeks = datemanager(skidate)
                it = iter(possibleSkiWeeks)
                finalweeks = []
                for x in it:
                    oneweek = [x, next(it)]
                    finalweeks.append(oneweek)
                scores = []
                stdDeviations = []
                numberOfItems = []
                locationNames = []
                for startDate,endDate in finalweeks:
                    oneWeekOfSking = snowAnalyzer(weathervaluesnorthamerica, startDate, endDate, int(deviationpenalty)).skiScorer()
                    ratedSkiPeriodWithLocation = skiresortlocater(oneWeekOfSking, stations).mergedatatoanalyze()
                    score, stdDeviation, numberofitems = visualizationofskidata(ratedSkiPeriodWithLocation, startDate, endDate).dataprep()
                    scores.append(score.values)
                    stdDeviations.append(stdDeviation.values)
                    numberOfItems.append(numberofitems)
                    locationNames.append(score.index)
                skiAreaBarChart(scores, stdDeviations, numberOfItems, locationNames)
                # break
                # skiAreaBarChart(scores)
            except Exception as e:
                raise
    except KeyboardInterrupt, ValueError:
        print "\n Interrupted!"
    except EOFError:
        print "\n Interrupted!"
