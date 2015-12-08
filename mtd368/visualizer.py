"""The visualizer module handles the process of generating the charts needed to evaluate
where a person should ski.  It does a small amount of data prep specific to the visualization
process, but is primarily concerned focused on visualizing the data."""

#author: Matthew Dunn
#netID: mtd368
#date: 12/12/2015

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class visualizationofskidata(object):
    def __init__(self, mergedSkiData, startDate, endDate):
        self.mergedSkiData = mergedSkiData.dropna(axis=0, how='any')
        self.startDate = startDate
        self.endDate = endDate

    def dataprep (self):
        stateCityIndex = self.mergedSkiData.set_index('StateCity', inplace=True)
        bigdumpscore = self.mergedSkiData['AverageScore2']
        bigdumpstd = self.mergedSkiData['std']
        bigdumpmean = self.mergedSkiData['mean']
        ind = np.arange(len(bigdumpscore))  # the x locations for the groups
        # finalmeanscores = self.mergedSkiData['AverageScore2']
        return bigdumpmean, bigdumpstd, ind

def skiAreaBarChart(listofscores, listofstdDeviations, listofNumberOfItems, locationNames):
    xmax = sorted(map(max, zip(*listofscores)))
    xmax = np.ceil(xmax[-1])+5  # Ensure the chart is large enough for the largest value.
    # build with a for loop - http://stackoverflow.com/questions/27569306/populating-matplotlib-subplots-through-a-loop-and-a-function
    width = 0.35
    plt.figure(1, tight_layout=True, figsize=(8,10))

    plt.subplot(5, 1, 1)
    plt.title('Two Weeks BEFORE to Entered Date')
    plt.barh(listofNumberOfItems[0], listofscores[0], width, align='center', color='r', xerr=listofstdDeviations[0], alpha=0.4)
    plt.yticks(listofNumberOfItems[0], locationNames[0])
    plt.xlim(0,xmax)
    plt.grid(True)

    plt.subplot(5, 1, 2)
    plt.title('One Week BEFORE to Entered Date')
    plt.barh(listofNumberOfItems[1], listofscores[1], width, align='center', color='y', xerr=listofstdDeviations[1], alpha=0.4)
    plt.yticks(listofNumberOfItems[1], locationNames[1])
    plt.xlim(0,xmax)
    plt.grid(True)

    plt.subplot(5, 1, 3)
    plt.title('Week of Entered Date')
    plt.barh(listofNumberOfItems[2], listofscores[2], width, align='center', color='g', xerr=listofstdDeviations[2], alpha=0.4)
    plt.yticks(listofNumberOfItems[2], locationNames[2])
    plt.xlim(0,xmax)
    plt.grid(True)

    plt.subplot(5, 1, 4)
    plt.title('One Week AFTER to Entered Date')
    plt.barh(listofNumberOfItems[3], listofscores[3], width, align='center', color='b', xerr=listofstdDeviations[3], alpha=0.4)
    plt.yticks(listofNumberOfItems[3], locationNames[3])
    plt.xlim(0,xmax)
    plt.grid(True)

    plt.subplot(5, 1, 5)
    plt.title('Two Weeks AFTER to Entered Date')
    plt.barh(listofNumberOfItems[4], listofscores[4], width, align='center', color='b', xerr=listofstdDeviations[4], alpha=0.4)
    plt.yticks(listofNumberOfItems[4], locationNames[4])
    plt.xlim(0,xmax)
    plt.grid(True)

    plt.show()
