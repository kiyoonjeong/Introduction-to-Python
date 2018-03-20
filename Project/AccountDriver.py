# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:20:17 2017

@author: Kiyoon Jeong
"""
import os

os.chdir("C:\\Users\\Kiyoon Jeong\\Desktop\\python\\CH9")

from account import account

def main():
    balance = int(input("Balance : "))
    test = account(balance)
    order = int(input("Enter 1 : Trade, 2 : process trades, 3 : Yesterday Price Range, 4 : Advance Day, 9 : Print Statement, 99 : Done :"))
    
    while order != 99:
        if order == 1:
            type = input("Type (sell or buy) : ")
            symbol = input("Symbol : ")
            offer = float(input("Offer : "))
            share = float(input("Share : "))
            test.trade(symbol, type, share, offer)
            order = int(input("Enter 1 : Trade, 2 : process trades, 3 : Yesterday Price Range, 4 : Advance Day, 9 : Print Statement, 99 : Done :"))

        elif order == 2:
            test.processTrades()
            test.advanceDay()
            order = int(input("Enter 1 : Trade, 2 : process trades, 3 : Yesterday Price Range, 4 : Advance Day, 9 : Print Statement, 99 : Done :"))
        
        elif order == 3:
            print(test.yesterdayPriceRange())
            order = int(input("Enter 1 : Trade, 2 : process trades, 3 : Yesterday Price Range, 4 : Advance Day, 9 : Print Statement, 99 : Done :"))
        
        elif order == 4:
            test.advanceDay()
            order = int(input("Enter 1 : Trade, 2 : process trades, 3 : Yesterday Price Range, 4 : Advance Day, 9 : Print Statement, 99 : Done :"))
            
        elif order == 9:
            test.printAccountStatement()
            order = int(input("Enter 1 : Trade, 2 : process trades, 3 : Yesterday Price Range, 4 : Advance Day, 9 : Print Statement, 99 : Done :"))
            
        else:
            print("Wrong Input")
            order = int(input("Enter 1 : Trade, 2 : process trades, 3 : Yesterday Price Range, 4 : Advance Day, 9 : Print Statement, 99 : Done :"))
            
    
        
        