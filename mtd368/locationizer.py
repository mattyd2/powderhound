"""The locationizer module merges NOAA analyzed data with location data of the
stations where the data was recorded. This enables the program to present the
state and city where the best skiing is in the united states."""

#author: Matthew Dunn
#netID: mtd368
#date: 12/12/2015

import os
import numpy as np
import pandas as pd

class skiresortlocater(object):

    def __init__ (self, rankedData, stations):
        self.rankedData = rankedData
        self.stations = stations

    def mergedatatoanalyze(self):
        weatherandstations = pd.merge(self.rankedData, self.stations, how='left', left_index=True, right_index=True)
        weatherandstations['StateCity'] = weatherandstations['STATE']+" "+weatherandstations['NAME']
        return weatherandstations


    #TO DO:

    # Append Nearest Ski Resort
        # Calculate distance from resorts to stations
            # Return the closest.

    # De-duplicate resorts -> creating forced rank
    # Return Top 5 Resorts to visualizer
