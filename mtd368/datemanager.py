"""ADD COMMENTS"""

#author: Matthew Dunn
#netID: mtd368
#date: 12/12/2015

import datetime
import calendar

def datemanager(inputString):
    validatedDate = validate(inputString)
    print validatedDate
    return datesrangenerator(inputString)

def validate(inputString):
    try:
        userinputskidate = datetime.datetime.strptime(inputString, '%Y-%m-%d')
        now = datetime.datetime.now()
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    if userinputskidate > now:
        return userinputskidate
    else:
        raise ValueError("Date must be in the future.")

def datesrangenerator(validatedDate):
    dayzero = datetime.datetime.strptime(validatedDate, '%Y-%m-%d')
    listofdayperiods = [-15,-9,-8,-1,0,6,7,13,14,20]
    weekperiods = []
    for i in listofdayperiods:
        datedelta = datetime.timedelta(days=i)
        changeddate = datedelta + dayzero
        weekperiods.append(changeddate)
    it = iter(weekperiods)
    finallist = []
    for x in it:
        temp = [x, next(it)]
        finallist.append(temp)
    # print finallist
    # print weekperiods
    return weekperiods

def numberOfDaysinStartMonth(startofweek):
    startofweekyear, startofweekmonth = startofweek.year, startofweek.month
    # endofweekyear, endofweekmonth = endofweek.year, endofweek.month
    startMonthLastDay = calendar.monthrange(startofweekyear,startofweekmonth)[1]
    # endmonthrange = calendar.monthrange(endofweekyear,endofweekmonth)[1]
    # print "start month %d and end month %d" % (startMonthLastDay, endmonthrange)
    numberofdaysinstartmonth = startMonthLastDay - startofweek.day
    # numberofdaysinendmonth = endofweek.day - endmonthrange
    return numberofdaysinstartmonth, startMonthLastDay
