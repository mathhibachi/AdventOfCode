# -*- coding: utf-8 -*-

from aocd import get_data
import math

# import pandas as pd
# import numpy as np

fin = 'day4Input2.txt'
data = get_data(day=4, year=2023).splitlines()

points = 0

cardCounts = {}

for line in data:
#with open(fin) as f:
#  for line in f.readlines():
      card = line.split(': ')[0].split(' ')[-1]
      print(int(card))
      cardCounts[int(card)] = 1

for line in data:
#with open(fin) as f:
#  for line in f.readlines():
    card = line.split(': ')[0].split(' ')[-1]
    winNums = line.split(': ')[1].split(' | ')[0].split(' ')
    winNums = [x.strip() for x in winNums if x != '']
    cardNums = line.split(': ')[1].split(' | ')[1].split(' ')
    cardNums = [x.strip() for x in cardNums if x != '']
    count = 0
    for cardNum in cardNums:
        if cardNum in winNums:
            count += 1
    
    for i in range(count):
        if i<len(cardCounts.keys())-1:
            cardCounts[int(card)+(i+1)] += 1 * cardCounts[int(card)]
    
    if count>0:
        print(card,count)
        points += cardCounts[int(card)] * 2**(count-1)
        
print(points)
print(cardCounts)

cardSums = 0
for k,v in cardCounts.items():
    cardSums+=v
print(cardSums)
