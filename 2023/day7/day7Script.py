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
                return 'onePair'
            else:
                return 'onePair'
        elif hand.count(card) == 1:
            if len(handUnique) == 5:
                return 'highCard'
            elif len(handUnique) == 2:
                return 'fourKind'
            elif len(handUnique) == 3:
                pairs = []
                for x in handUnique:
                    if x == card:
                        continue
                    elif hand.count(x) == 3:
                        return 'threeKind'
                    elif hand.count(x) == 2 and x not in pairs:
                        pairs.append(x)
                    else:
                        continue
                if len(pairs) == 2:
                    return 'twoPair'
                elif len(pairs) == 1:
                    return 'onePair'
                return 'highCard'
            elif len(handUnique) == 4:
                return 'onePair'
            else:
                return 'highCard'
            
        else:
            return 'N/A'

#exData.append('J488Q 100')
handPoints = {}
hands = []
for i,line in enumerate(exData):
    [hand,bid] = line.split(' ')
    # print(hand,end=': ')
    handType = getHandType(hand)
    handPoints = handRanks[handType]
    hands.append([hand,bid,handType,handPoints])

sortedHands = sorted(hands, key=lambda hand: hand[3], reverse=True)

for i,hand in enumerate(sortedHands):
    print(hand[0],hand[1],hand[2],hand[3])
    
