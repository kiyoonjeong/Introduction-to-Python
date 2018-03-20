# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:13:35 2017

@author: Kiyoon Jeong
"""
import os

os.chdir("C:\\Users\\Kiyoon Jeong\\Desktop\\python\\CH9")

from MarketSimulation import MarketSimulation
from market import Market

market = MarketSimulation()
multi = Market()

class account:
    global market
    global multi
    
    def __init__(self, balance):
        self._balance = balance
        self._tradehistory = []
        self._holding = dict()
    
    def trade(self, symbol, type, shares, offer):
        if symbol == "T"
        if type == "buy":
            if self._balance >= offer*shares:
                if market.executableBuyTrade(offer):
                    multi.trade(symbol,type,shares, offer)
                    self._balance -= offer*shares
                    trade = "buy" + "," + str(shares) + "," + str(offer)
                    self._tradehistory.append(trade)
                    if symbol in self._holding:
                        self._holding[symbol] += shares
                    else :
                        self._holding[symbol] = shares
                    print("Trade Executed : True")
                else :
                    print("Trade Executed : False")    
            else:
                print("Not enough balance")
    
        if type == "sell":
            if symbol in self._holding:
                if self._holding[symbol] >= shares:
                    if market.executableSellTrade(offer):
                        multi.trade(symbol,type,shares, offer)
                        self._balance += offer*shares
                        trade = "sell" + "," + str(shares) + "," + str(offer)
                        self._tradehistory.append(trade)
                        self._holding[symbol] -= shares
                        print("Trade Executed : True")
                    else :
                        print("Trade Executed : False")
                else:
                    print("Not enough shares")
            else:
                print("No avaiable shares for that symbol")

    def printAccountStatement(self):
        print("Balance = ", self._balance, "," , "Trade History = ", self._tradehistory, "," , "Holding shares = ", self._holding)
    
    def processTrades(self):
        print(multi._trade)
    
    def advanceDay(self):
        multi._trade = []
        market.advanceDay()
    
    def yesterdayPriceRange(self):
        return market.getRange()
        
            
        