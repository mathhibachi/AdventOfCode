# -*- coding: utf-8 -*-
from aocd.models import Puzzle
import numpy as np

puz = Puzzle(year=2023,day=15)
# Example input data
exData = puz.example_data
# Full input data
inData = puz.input_data

# If reading in from local file
# exData2 = []
# with open('day13Input2.txt') as f:
#   for line in f.readlines():
#     exData2.append(line.strip())

exData = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

# Set data set to use for testing
data = inData.split(',')

def getValue(x):
    curValue = 0
    for y in x:
        #print(y)
        curValue += ord(y)
        curValue *= 17
        curValue = curValue % 256
    return curValue

sums = []
for x in data:
    curValue = getValue(x)    
    sums.append(curValue)
#print(sums)
print(sum(sums))

boxes = [{} for i in range(256)]
lenses = []
for x in data:
    if '=' in x:
        y = x.split('=')[0]
        if y not in lenses:
            lenses.append(y)
        boxes[getValue(y)][y] = x.split('=')[1]
    elif '-' in x:
        y = x.split('-')[0]
        if y not in lenses:
            lenses.append(y)
        if y in boxes[getValue(y)].keys():
            del(boxes[getValue(y)][y])
    #print(y,getValue(y))
newSums = []   
for lens in lenses:
    if lens in boxes[getValue(lens)]:
        a = getValue(lens)+1
        b = list(boxes[getValue(lens)]).index(lens)+1
        c = int(boxes[getValue(lens)][lens])
        #print(lens,a,b,c,str(a*b*c))
        newSums.append(a*b*c)
#print(newSums)
print(sum(newSums))
