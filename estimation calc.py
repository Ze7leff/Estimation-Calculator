# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:33:05 2022

@author: Adam
"""


def playerNames():
    _1, _2, _3, _4 = "Player1", "Player2", "Player3", "Player4"
    print("type 'done' to choose calls")
    choice = input("choose player number: \n(1 or 2 or 3 or 4)\n")
    print("type 'done' to choose calls")
    while choice != "done":
       if choice == "1":
           _1 = input("Player1 name: ")
           print(_1, _2, _3, _4)
           choice = input("choose player number: (1 or 2 or 3 or 4)\n")
       elif choice == "2":
           _2 = input("Player2 name: ")
           print(_1, _2, _3, _4)
           choice = input("choose player number: (1 or 2 or 3 or 4)\n")
       elif choice == "3":
           _3 = input("Player3 name: ")
           print(_1, _2, _3, _4)
           choice = input("choose player number: (1 or 2 or 3 or 4)\n")
       elif choice == "4":
           _4 = input("Player4 name: ")
           print(_1, _2, _3, _4)
           choice = input("choose player number: (1 or 2 or 3 or 4)\n")
       else:
           print("try again")
           choice = input("choose player number: (1 or 2 or 3 or 4)\n")
    print(_1, _2, _3, _4)
    return [_1, _2, _3, _4]
    


def riskCheck(HighestBid, Players):
    pos = 0
    newlst = [] 
    for i in range(len(Players)):
        if Players[i] == HighestBid[0]:
            pos = i
            break
    if pos != 0:
        newlst = Players[pos: ] + Players[ :pos]
        risk = newlst[-1]
    else:
        risk = Players[3]
    return risk



def highestBid(Players):
    choice = input("highest bid: ")
    while choice not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']:
        print('try again')
        choice = input("highest bid: ")
    suit = input("suit: ")
    while suit not in ['Suns', 'Trefle', 'Spade', 'Heart', 'Diamond']:
        print('try again')
        suit = input("suit: ")
    if suit == "Suns":
        suit = u"\u2600"
    if suit == "Trefle":
        suit = u"\u2663"
    if suit == "Spade":
        suit = u"\u2660"
    if suit == "Heart":
        suit = u"\u2665"
    if suit == "Diamond":
       suit = u"\u2666"
    choice2 = input("player: ")
    while choice2 not in Players:
        print('try again')
        choice2 = input("player: ")
    return [choice2, choice, suit]


Players = playerNames()  
HighestBid = highestBid(Players)
hasRisk = riskCheck(HighestBid, Players)    
    
def GameBoard(Players, Calls):
    print(Players[0] +" | "+ Players[1], "|", Players[2], "|", Players[3])
    print("-" * (len(Players[0])), " ", "-" * (len(Players[0])), " ","-" * (len(Players[0])), " ","-" * (len(Players[0])))
    print(" "*(len(Players[0])//2)+Calls[0]+" "*(len(Players[0])//2)+"| |"+" "*(len(Players[0])//2)+Calls[0]+" "*(len(Players[0])//2)+"| |"+" "*(len(Players[0])//2)+Calls[0]+" "*(len(Players[0])//2)+"| |"+" "*(len(Players[0])//2)+Calls[0]+" "*(len(Players[0])//2)+"| |")
    
    
    
    
    
    
    