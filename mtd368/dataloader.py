"""The dataloader module creates a snow.txt file from a larger set of text files
then loads the snow.txt file into a dataframe. Once the data is loaded into the
dataframe, functions clean the and prepare the dataframe for analysis."""

#author: Matthew Dunn
#netID: mtd368
#date: 12/12/2015

import os
import numpy as np
import pandas as pd

def loaddata():
    newfile = os.path.isfile("snow.txt")
    if newfile == False:
        print "Creating snow.txt file from 3.7GB of NOAA text data, this could take a min........\n"
        weathermeasurementtypefilebuilder() # this can be run each time or just once beacause it creates a text file with all the data for a specific precipitation type, currently set to SNOW.

def weathermeasurementtypefilebuilder ():
    dataDirectoryPath = os.path.join(os.path.dirname(__file__), os.pardir, 'ghcnd_hcn')
    newfile = open("snow.txt", 'w')
    for i in os.listdir(dataDirectoryPath):
        filename = dataDirectoryPath+'/'+i
        infile = open(filename)
        for line in infile:
            element = line[17:21]
            if element == 'SNOW':
                newfile.write(line)
        infile.close()
    newfile.close()

def monthlytextweatherdatamunger ():
    print "Loading Data snow.txt file data into dataframe...............\n"
    precipitationFileName = 'snow.txt'
    splits = [[0,11],[11,15],[15,17],[17,21],[21,26],[26,27],[27,28],[28,29],[29,34],[34,35],[35,36],[36,37],[37,42],[42,43],[43,44],[44,45],[45,50],[50,51],[51,52],[52,53],[53,58],[58,59],[59,60],[60,61],[61,66],[66,67],[67,68],[68,69],[69,74],[74,75],[75,76],[76,77],[77,82],[82,83],[83,84],[84,85],[85,90],[90,91],[91,92],[92,93],[93,98],[98,99],[99,100],[100,101],[101,106],[106,107],[107,108],[108,109],[109,114],[114,115],[115,116],[116,117],[117,122],[122,123],[123,124],[124,125],[125,130],[130,131],[131,132],[132,133],[133,138],[138,139],[139,140],[140,141],[141,146],[146,147],[147,148],[148,149],[149,154],[154,155],[155,156],[156,157],[157,162],[162,163],[163,164],[164,165],[165,170],[170,171],[171,172],[172,173],[173,178],[178,179],[179,180],[180,181],[181,186],[186,187],[187,188],[188,189],[189,194],[194,195],[195,196],[196,197],[197,202],[202,203],[203,204],[204,205],[205,210],[210,211],[211,212],[212,213],[213,218],[218,219],[219,220],[220,221],[221,226],[226,227],[227,228],[228,229],[229,234],[234,235],[235,236],[236,237],[237,242],[242,243],[243,244],[244,245],[245,250],[250,251],[251,252],[252,253],[253,258],[258,259],[259,260],[260,261],[261,266],[266,267],[267,268],[268,269]]
    monthlyWeather = splitter(splits, precipitationFileName)
    monthlyWeather.columns = ['Station','Year','Month','Snow','Day01','MFLAG1','QFLAG1','SFLAG1','Day02','MFLAG2','QFLAG2','SFLAG2','Day03','MFLAG3','QFLAG3','SFLAG3','Day04','MFLAG4','QFLAG4','SFLAG4','Day05','MFLAG5','QFLAG5','SFLAG5','Day06','MFLAG6','QFLAG6','SFLAG6','Day07','MFLAG7','QFLAG7','SFLAG7','Day08','MFLAG8','QFLAG8','SFLAG8','Day09','MFLAG9','QFLAG9','SFLAG9','Day10','MFLAG10','QFLAG10','SFLAG10','Day11','MFLAG11','QFLAG11','SFLAG11','Day12','MFLAG12','QFLAG12','SFLAG12','Day13','MFLAG13','QFLAG13','SFLAG13','Day14','MFLAG14','QFLAG14','SFLAG14','Day15','MFLAG15','QFLAG15','SFLAG15','Day16','MFLAG16','QFLAG16','SFLAG16','Day17','MFLAG17','QFLAG17','SFLAG17','Day18','MFLAG18','QFLAG18','SFLAG18','Day19','MFLAG19','QFLAG19','SFLAG19','Day20','MFLAG20','QFLAG20','SFLAG20','Day21','MFLAG21','QFLAG21','SFLAG21','Day22','MFLAG22','QFLAG22','SFLAG22','Day23','MFLAG23','QFLAG23','SFLAG23','Day24','MFLAG24','QFLAG24','SFLAG24','Day25','MFLAG25','QFLAG25','SFLAG25','Day26','MFLAG26','QFLAG26','SFLAG26','Day27','MFLAG27','QFLAG27','SFLAG27','Day28','MFLAG28','QFLAG28','SFLAG28','Day29','MFLAG29','QFLAG29','SFLAG29','Day30','MFLAG30','QFLAG30','SFLAG30','Day31','MFLAG31','QFLAG31','SFLAG31']
    monthlyWeather[['Month','Day01','Day02','Day03','Day04','Day05','Day06','Day07','Day08','Day09','Day10','Day11','Day12','Day13','Day14','Day15','Day16','Day17','Day18','Day19','Day20','Day21','Day22','Day23','Day24','Day25','Day26','Day27','Day28','Day29','Day30','Day31']] = monthlyWeather[['Month','Day01','Day02','Day03','Day04','Day05','Day06','Day07','Day08','Day09','Day10','Day11','Day12','Day13','Day14','Day15','Day16','Day17','Day18','Day19','Day20','Day21','Day22','Day23','Day24','Day25','Day26','Day27','Day28','Day29','Day30','Day31']].astype(float)
    monthlyWeather.replace(to_replace=-9999, value=np.nan, inplace=True)
    columnsToDrop = ['MFLAG1','QFLAG1','SFLAG1','MFLAG2','QFLAG2','SFLAG2','MFLAG3','QFLAG3','SFLAG3','MFLAG4','QFLAG4','SFLAG4','MFLAG5','QFLAG5','SFLAG5','MFLAG6','QFLAG6','SFLAG6','MFLAG7','QFLAG7','SFLAG7','MFLAG8','QFLAG8','SFLAG8','MFLAG9','QFLAG9','SFLAG9','MFLAG10','QFLAG10','SFLAG10','MFLAG11','QFLAG11','SFLAG11','MFLAG12','QFLAG12','SFLAG12','MFLAG13','QFLAG13','SFLAG13','MFLAG14','QFLAG14','SFLAG14','MFLAG15','QFLAG15','SFLAG15','MFLAG16','QFLAG16','SFLAG16','MFLAG17','QFLAG17','SFLAG17','MFLAG18','QFLAG18','SFLAG18','MFLAG19','QFLAG19','SFLAG19','MFLAG20','QFLAG20','SFLAG20','MFLAG21','QFLAG21','SFLAG21','MFLAG22','QFLAG22','SFLAG22','MFLAG23','QFLAG23','SFLAG23','MFLAG24','QFLAG24','SFLAG24','MFLAG25','QFLAG25','SFLAG25','MFLAG26','QFLAG26','SFLAG26','MFLAG27','QFLAG27','SFLAG27','MFLAG28','QFLAG28','SFLAG28','MFLAG29','QFLAG29','SFLAG29','MFLAG30','QFLAG30','SFLAG30','MFLAG31','QFLAG31','SFLAG31']
    monthlyWeather = monthlyWeather.drop(columnsToDrop,axis=1)
    monthlyWeather['UniqueStationByYear'] = monthlyWeather['Station']+monthlyWeather['Year']
    monthlyWeather.set_index(monthlyWeather.UniqueStationByYear, inplace=True)
    monthlyWeather = monthlyWeather.drop('UniqueStationByYear',axis=1)
    return monthlyWeather

def staiondatamunger():
    print "Loading Sation data into dataframe...............\n"
    stationsFileName = 'ghcnd-stations.txt'
    splits = [[0,11],[12,20],[21,30],[31,37],[38,40],[41,71],[72,75],[76,79],[80,85]]
    weatherStations = splitter(splits, stationsFileName)
    weatherStations.columns = ['Station', 'LAT', 'LONG', 'ELEV', 'STATE', 'NAME', 'GSNFLAG','HCNFLAG','WMOID']
    weatherStations = weatherStations.set_index('Station')
    return weatherStations

def splitter(splits, fileToBeSplitName):
    fileToBeSplitData = pd.read_csv(fileToBeSplitName, delimiter='\n', dtype=str, squeeze=True, header=None)
    splitDataRepository = pd.DataFrame([])
    for i,j in splits:
        splitname = "split["+str(i)+':'+str(j)+']'
        splitDataRepository[splitname] = fileToBeSplitData.str[slice(i,j)]
    return splitDataRepository
