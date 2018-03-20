# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:22:39 2017

@author: Kiyoon Jeong
"""
import os

os.chdir("C:\\Users\\Kiyoon Jeong\\Desktop\\python\\CH9")

from MarketSimulation import MarketSimulation

def main():
    test = MarketSimulation()
    i = int(input("1 = Get Yesterdays Closing Data, 2 = Executable Buy Trade, 3 = Executable Sell Trade, 4 = Advance Day , 5 = YesterdayRange , -1 = End : "))
    while i != -1:
        if i == 1:
            print(test.getYesterDaysClosingData())
            i = int(input("1 = Get Yesterdays Closing Data, 2 = Executable Buy Trade, 3 = Executable Sell Trade, 4 = Advance Day , 5 = YesterdayRange , -1 = End : "))
        elif i == 2:
            offer = int(input("Please input offer to buy price :"))
            print(test.executableBuyTrade(offer))
            test.advanceDay()
            i = int(input("1 = Get Yesterdays Closing Data, 2 = Executable Buy Trade, 3 = Executable Sell Trade, 4 = Advance Day , 5 = YesterdayRange , -1 = End : "))
        elif i == 3:
            offer = int(input("Please input offer to sell price :"))
            print(test.executableSellTrade(offer))
            test.advanceDay()
            i = int(input("1 = Get Yesterdays Closing Data, 2 = Executable Buy Trade, 3 = Executable Sell Trade, 4 = Advance Day , 5 = YesterdayRange , -1 = End : "))
        elif i == 4:
            test.advanceDay()
            i = int(input("1 = Get Yesterdays Closing Data, 2 = Executable Buy Trade, 3 = Executable Sell Trade, 4 = Advance Day , 5 = YesterdayRange , -1 = End : "))
        elif i == 5:
            range = test.getRange()
            print(range)
            i = int(input("1 = Get Yesterdays Closing Data, 2 = Executable Buy Trade, 3 = Executable Sell Trade, 4 = Advance Day ,  5 = YesterdayRange , -1 = End : "))
        else :
            print("Wrong Input")
            i = int(input("1 = Get Yesterdays Closing Data, 2 = Executable Buy Trade, 3 = Executable Sell Trade, 4 = Advance Day ,  5 = YesterdayRange , -1 = End : "))
main()