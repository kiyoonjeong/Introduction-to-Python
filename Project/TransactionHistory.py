# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:37:14 2017

@author: Kiyoon Jeong
"""
from PerformanceData import PerformanceData

class TransactionHistory :
    #open the file and get the list of values
    def __init__(self, filename) :
        inputFile = open(filename, "r")
        #list of transaction history
        self._hist = []
        for line in inputFile:
            line = line.rstrip()
            line = line.split(",")
            perform = PerformanceData(line[0],line[1],line[2],line[3], line[4],line[5])
            self._hist.insert(0,perform.__str__())
        self._hist.pop(len(self._hist)-1)
    
    #get the value of the specific date's history
    def getHistory(self, integer) :
        return self._hist[integer]
            