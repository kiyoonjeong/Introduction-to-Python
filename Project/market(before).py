# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:03:44 2017

@author: Kiyoon Jeong
"""

import os

os.chdir("C:\\Users\\Kiyoon Jeong\\Desktop\\python\\CH9")

from MarketSimulation import MarketSimulation
from Trade import Trade

market = MarketSimulation()

class Market:
    global market
    def __init__(self):
        self._trade = []
            
    def trade(self, symbol, type, shares, offer):
        t = Trade(symbol, type, shares, offer)
        self._trade.append(t.__str__())
                
    def processTrades(self):
        return self._trade