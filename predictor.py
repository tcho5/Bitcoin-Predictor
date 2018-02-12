# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:39:12 2018

@author: Daniel Lee
"""
#import pandas as pd
from FileParser import FileParser

"""
This function tries to predict whether the stock will increase or decrease by seeing the current trend 
(slope of 3 recent data points) and comparing if past similar trends (slopes of all past 3 data points)
increased more or decreased more
"""
DEBUG = False

def predict():
    fileParser = FileParser()
    table = fileParser.parse("predictor")
    maxSize = fileParser.getMax()
    #print(maxSize)
    epsilon = .6 #percent error
    dataContainer = []
    
    for i in range(0, maxSize):
        openValue = table.iloc[i, 0]
        closeValue = table.iloc[i, 1]
        percentDifference = (closeValue - openValue) / openValue * 100
        dataContainer.append(percentDifference) #stores the percent difference between the closed and open value
    
    if DEBUG:
        print(table)

    accumMatch = 0
    accumIncrease = 0
    #averages the current 3 percent differences
    currentAvg = (dataContainer[maxSize - 1] + dataContainer[maxSize - 2] + dataContainer[maxSize - 3]) / 3
    if DEBUG:
        print("\"\"\"DEBUG START\"\"\"")
        print("LAST THREE DIFFERENCE:")
        #print("1.", dataContainer[0])
        print("1.", dataContainer[maxSize - 1])
        print("2.", dataContainer[maxSize - 2])
        print("3.", dataContainer[maxSize - 3])
        print("CURRENT AVG:", currentAvg)
        
    for i in range(2, maxSize - 1):
        #gets the averages of all the past 3 percent differences and checks if the trend 
        #is similar to the current average with margin of error (epsilon)
        pastAvg = (dataContainer[i] + dataContainer[i - 1] + dataContainer[i - 2]) / 3
        if currentAvg - epsilon < pastAvg and currentAvg + epsilon > pastAvg:
            accumMatch += 1
            #within those similar trends, check how much of those events actually increased afterwards
            if dataContainer[i + 1] > 0:
                accumIncrease += 1
    #This means that there was no similar trends, then give a 50:50 prediction
    if accumMatch == 0:
        return(.5, .5)
        
    probabilityIncrease = accumIncrease / accumMatch
    probabilityDecrease = (accumMatch - accumIncrease) / accumMatch
    
    if DEBUG:
        print("ACCUM INCREASE:", accumIncrease)
        print("ACCUM MATCH:", accumMatch)
        print("PROBABILITY TO INCREASE:", probabilityIncrease)
        print("PROBABILITY TO DECREASE:", probabilityDecrease)
        print("\"\"\"DEBUG END\"\"\"")
    
    return(probabilityIncrease, probabilityDecrease)
