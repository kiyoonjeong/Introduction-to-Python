# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:22:50 2017

@author: Kiyoon Jeong
"""
import os

os.chdir("C:\\Users\\Kiyoon Jeong\\Desktop\\python\\CH9")

class Trade:
    def __init__(self, symbol, type, shares, offer):
        self._symbol = symbol
        self._type = type
        self._shares = shares
        self._offer = offer

    def getSymbol(self):
        return self._symbol
    
    def getType(self):
        return self._type
    
    def getShares(self):
        return self._shares
        
    def getOffer(self):
        return self._offer
        
    def __str__(self):
        return self._symbol + ',' + self._type + ',' + str(self._shares) + ',' + str(self._offer)


        