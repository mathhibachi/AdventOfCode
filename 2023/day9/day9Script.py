# -*- coding: utf-8 -*-
from aocd.models import Puzzle

puz = Puzzle(year=2023,day=9)
# Example input data
exData = puz.example_data.splitlines()
# Full input data
inData = puz.input_data.splitlines()

# If reading in from local file
# exData2 = []
# with open('day9Input3.txt') as f:
#   for line in f.readlines():
#       exData2.append(line.strip())

# Set data set to use for testing
data = exData

def getDiffs(line):
    diffs = []
    for i,x in enumerate(line):
        if i < len(line)-1:
            diff = line[i+1]-line[i]
            diffs.append(diff)
    return diffs

valueSum = 0
valueDiff = 0
newLines = []
for line in data:
    newLine = [int(x) for x in line.split(' ')]
    
    # Input line ([10, 13, 16, 21, 30, 45])
    newLines.append(newLine)
    
    # Newer lines list will append a line below with the differences between
    #  numbers reach 0
    #   [10, 13, 16, 21, 30, 45]
    #     [3, 3, 5, 9, 15]
    #       [0, 2, 4, 6]
    #         [2, 2, 2]
    #           [0, 0]
    newerLines = []
    newerLines.append(newLine)
    diffs = getDiffs(newLine)
    newerLines.append(diffs)
    while False in [x==0 for x in diffs]:
        diffs = getDiffs(diffs)
        newerLines.append(diffs)
    
    values = [0 for x in range(len(newerLines))]
    for i in range(len(newerLines)-2,-1,-1):
        #print(newerLines[i][-1] + newerLines[i+1][-1])
        values[i] = newerLines[i][-1] + values[i+1]
    #print(values)
    valueSum += values[0]
    
    values = [0 for x in range(len(newerLines))]
    for i in range(len(newerLines)-2,-1,-1):
        #print(newerLines[i][0] - values[i+1])
        values[i] = newerLines[i][0] - values[i+1]
    #print(values)
    valueDiff += values[0]
    
print(valueSum)
print(valueDiff)    
