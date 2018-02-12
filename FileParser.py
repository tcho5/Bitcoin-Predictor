     # -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:48:35 2018

@author: Daniel Lee
"""
import pandas as pd
import webScraper

class FileParser():
    def __init__(self):
        self.__maxSize = webScraper.createCSV()
        
        rtable = pd.read_csv("coinmarket.csv")
        self.__table = rtable.iloc[::-1]
        
    def parse(self, type):
        if type == "predictor":
            return self.__table[["OPEN", "CLOSE"]]
        elif type == "graph":
            return self.__table[["DATE", "CLOSE"]]
    
    def getMax(self):
        return self.__maxSize

"""   
def main():
    file = FileParser()
    table = file.parse("predictor")
    print(table)

main()
"""
