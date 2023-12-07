# -*- coding: utf-8 -*-

from aocd.models import Puzzle

puz = Puzzle(year=2023,day=7)
# Example input data
exData = puz.example_data.splitlines()
# Full input data
inData = puz.input_data.splitlines()

handRanks = {'fiveKind':7,'fourKind':6,'fullHouse':5,'threeKind':4,
             'twoPair':3,'onePair':2,'highCard':1}

def getHandType(hand):
    #cards = [card for card in hand]
    handUnique = set(hand)

    for card in hand:
        if hand.count(card) == 5:
            return 'fiveKind'
        elif hand.count(card) == 4:
            return 'fourKind'
        elif hand.count(card) == 3:
            if len(handUnique) == 2:
                return 'fullHouse'
            else:
                return 'threeKind'
        elif hand.count(card) == 2:
            if len(handUnique) == 2:
                return 'fullHouse'
            elif len(handUnique) == 3:
                for x in handUnique:
                    if x == card:
                        continue
                    elif hand.count(x) == 2:
                        return 'twoPair'
        else:
            return 'N/A'
        
for line in exData:
    [hand,bid] = line.split(' ')
    print(hand,end=': ')
    print(getHandType(hand))
    
