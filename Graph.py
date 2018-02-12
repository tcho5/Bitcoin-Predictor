# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:18:37 2018

@author: Daniel Lee
"""
import matplotlib.pyplot as plt
from FileParser import FileParser

"""
Creates the graph to show the prices/hours of Bitcoin 
"""
class Graph():
    def __init__(self):
        fileParser = FileParser()
        self.__table = fileParser.parse("graph")
        self.__maxSize = fileParser.getMax()
        self.__price = []
        self.__date = []
        self.__range = 365
        
    def saveGraph(self):
        ctr = []
        fig = plt.figure()
        title = "Bitcoin Price Values (USD) Over The Past " + str(self.__range) + " Days"
        for i in range(self.__maxSize - self.__range, self.__maxSize):
            self.__date.append(self.__table.iloc[i, 0])
            self.__price.append(self.__table.iloc[i, 1])
            ctr.append(i)
       
        # plotting the points 
        plt.plot(ctr, self.__price)
        #plt.plot(self.__date, self.__low, label = "Low Points")
        
        plt.xlabel("Past Year")
        plt.xticks([])
        plt.ylabel("Price (USD)")
        plt.title(title)
        fig.savefig("Graph.png")

"""
def main():
    graph = Graph()
    graph.saveGraph()
    
main()
"""

