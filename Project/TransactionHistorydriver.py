# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:03:14 2017

@author: Kiyoon Jeong
"""

from TransactionHistory import TransactionHistory

test = TransactionHistory("T.csv")

def main():
    check = int(input("Please input 0 or positive integer. To end, input -1: "))
    while check != -1:
        print(test.getHistory(check))
        return main()

main()