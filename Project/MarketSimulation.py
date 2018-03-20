# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:35:15 2017

@author: Kiyoon Jeong
"""
import os

os.chdir("C:\\Users\\Kiyoon Jeong\\Desktop\\python\\CH9")

from TransactionHistory import TransactionHistory

class MarketSimulation :
    #construct currentday, yesterday, high value, low value, and close value
    def __init__(self):
        self._currentDay = 1
        self._yesterday = 0
        
        hist = TransactionHistory("T.csv")
        yesterdayData = hist.getHistory(self._yesterday)
        yesterdayData = yesterdayData.split(",")
        
        currentData = hist.getHistory(self._currentDay)
        currentData = currentData.split(",")
        
        self._high = currentData[2]
        self._low = currentData[3]
        self._close = yesterdayData[4]
        self._range = str(yesterdayData[3]) + '-' + str(yesterdayData[2])

    #get the close value
    def getYesterDaysClosingData(self):
        return self._close
    
    #check if the buy trade is executable
    def executableBuyTrade(self, offer):
        if float(offer) >= float(self._low):
            return True
        else :
            return False
    
    #check if the sell trade is executable
    def executableSellTrade(self, offer):
        if float(offer) <= float(self._high):
            return True
        else :
            return False
    
    # Increments the currentday and yesterday
    # Also, update the high, low, and close value
    def advanceDay(self):
        self._currentDay += 1
        self._yesterday += 1
        
        hist = TransactionHistory("T.csv")
        yesterdayData = hist.getHistory(self._yesterday)
        yesterdayData = yesterdayData.split(",")
        
        currentData = hist.getHistory(self._currentDay)
        currentData = currentData.split(",")
        
        self._high = currentData[2]
        self._low = currentData[3]
        self._close = yesterdayData[4]
        self._range = str(yesterdayData[3]) + '-' + str(yesterdayData[2])

    def getRange(self):
        return self._range
        
        