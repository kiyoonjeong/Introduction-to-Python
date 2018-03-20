# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:47:36 2017

@author: Kiyoon Jeong
"""

class PerformanceData :
    #construct date, open, close, high, low, and volume
    def __init__(self, date, open, close, high, low, volume) :
        self._date = str(date)
        self._open = open
        self._close = close
        self._high = high
        self._low = low
        self._volume = volume
    
    #get the date value
    def getDate(self) :
        return self._date
    #get the open value
    def getOpen(self) :
        return self._open
    #get the close value
    def getClose(self) :
        return self._close
    #get the high value
    def getHigh(self) :
        return self._high
    #get the low value
    def getLow(self) :
        return self._low
    #get the volume
    def getVolume(self) :
        return self._volume
    
    # print the values
    def __str__(self):
        return str(self._date) + "," + str(self._open) + "," + str(self._close) + "," + str(self._high) + "," + str(self._low) + "," + str(self._volume)
        