# -*- coding: utf-8 -*-

from aocd import get_data
import math

# import pandas as pd
# import numpy as np

fin = 'day4Input2.txt'
data = get_data(day=4, year=2023).splitlines()

points = 0

[cardCounts[x] = 1 for x in data]

with open(fin) as f:
  for line in f.readlines():

# for line in data:
    card = line.split(': ')[0].split(' ')[1]
    winNums = line.split(': ')[1].split(' | ')[0].split(' ')
    winNums = [x.strip() for x in winNums if x != '']
    cardNums = line.split(': ')[1].split(' | ')[1].split(' ')
    cardNums = [x.strip() for x in cardNums if x != '']
    count = 0
    for cardNum in cardNums:
        if cardNum in winNums:
            count += 1
    
    
    if count>0:
        print(card,count)
        points += 2**(count-1)
        
print(points)
