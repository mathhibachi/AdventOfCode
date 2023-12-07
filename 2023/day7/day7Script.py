# -*- coding: utf-8 -*-

from aocd.models import Puzzle

puz = Puzzle(year=2023,day=7)
# Example input data
exData = puz.examples[0].input_data.splitlines()
# Full input data
inData = puz.input_data.splitlines()

handRanks = {'fiveKind':7,'fourKind':6,'fullHouse':5,'threeKind':4,
             'twoPair':3,'onePair':2,'highCard':1}

cardRanks = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
             'T':10,'J':11,'Q':12,'K':13,'A':14}

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
for i,line in enumerate(inData):
    [hand,bid] = line.split(' ')
    # print(hand,end=': ')
    handType = getHandType(hand)
    handPoints = handRanks[handType]
    cardPoints = []
    for card in hand:
        cardPoints.append(cardRanks[card])
    hands.append([hand,bid,handType,handPoints,cardPoints])

sortedHands = sorted(hands, key=lambda hand: hand[3])

# for i,hand in enumerate(sortedHands):
#     print(hand[0],hand[1],hand[2],hand[3])

# newHands = {}
# for i in handRanks.values():
#     if i in set([hand[3] for hand in sortedHands]):
#         newHands[i] = [hand for hand in sortedHands if hand[3]==i]

newHands = {}
for hand in sortedHands:
    if hand[3] not in newHands.keys():
        newHands[hand[3]] = []
    newHands[hand[3]].append(hand)
#newerHands = sorted(hands, key = lambda hand: sorted(hand[3],
#                key = lambda card: (card[0],card[1],card[2],
#                                         card[3],card[4])), reverse=True)

newerHands = {}
count = 1
for i in newHands.keys():
    print(sorted(newHands[i], key = lambda card: card[4]))
    temp = sorted(newHands[i], key = lambda card: card[4])
    for hand in temp:
        newerHands[count] = count*int(hand[1])
        count+=1
    
#     thing = []
#     for hand in newHands[i]:
#         print(sorted(hand))
#         thing.append(hand[4])
#     sortedThing = sorted(thing, reverse=True,
#                          key=lambda card: (card[0],card[1],card[2],
#                                                   card[3],card[4]))
#     newerHands[i] = sortedThing

print(newerHands)
print(sum(newerHands.values()))
