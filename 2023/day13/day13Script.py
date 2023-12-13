# -*- coding: utf-8 -*-
from aocd.models import Puzzle
#import numpy as np

puz = Puzzle(year=2023,day=13)
# Example input data
#exData = puz.example_data.splitlines()
exData = puz.examples[0].input_data.splitlines()
# Full input data
inData = puz.input_data.splitlines()

# If reading in from local file
# exData2 = []
# with open('day13Input2.txt') as f:
#   for line in f.readlines():
#     exData2.append(line.strip())

# Set data set to use for testing
data = exData

def transpose(x):
    return list(map(list, zip(*x)))

def solvePattern(pattern,rowFlag,y):
    found = False
    for i in range(len(pattern)-1):
        smudges = 0
        # for j in range(len(pattern)-1):
           
        #     if j+1+(j-i) in range(len(pattern)) and \
        #                   pattern[i] != pattern[j+1+(j-i)]:
        if pattern[i+1] == pattern[i]:
            stopRng = min(i,len(pattern)-(i+1))
            found2 = True
            for j in range(1,stopRng):
              if pattern[i-j] != pattern[(i+1)+j]:
                  found2 = False
            if found2:
                found = True
                if rowFlag:
                    print('Found in row ',i+1)
                    return 100*(i+1)
                else:
                    print('Found in col ',i+1)
                    return i+1
    if not found:
        print('Pattern not found')
        return 0
   

count = 0
newData = {}
rowSums = {}

for line in data:
    if len(line)>0:
        if count not in newData.keys():
            newData[count] = []
            rowSums[count] = 0
        newData[count].append(line)
    else:
        temp = solvePattern(transpose(newData[count]),False,0)
        if temp > 0:
            rowSums[count] += temp
            count += 1
            newData[count] = []
            rowSums[count] = 0
        else:
            rowSums[count] += solvePattern(newData[count],True,0)
            count += 1
            newData[count] = []
            rowSums[count] = 0

temp = solvePattern(transpose(newData[count]),False,0)
if temp > 0:
    rowSums[count] += temp
else:
    rowSums[count] += solvePattern(newData[count],True,0)

print(rowSums)
print(sum(rowSums.values()))

# npData = np.array([])
# for row in data:
#     if len(row)>0:
#         if len(npData) == 0:
#             npData = np.array([row])
#         else:
#             npData = np.vstack((npData,row))
#     else:
#         print(npData)
#         npData = np.array([])

# def solvePattern(pattern, y):
# pattern = ["".join(x) for x in pattern]
# for i in range(len(pattern)-1):
# # reflect [0...i] to [i+1...len(pattern)-1]
# smudges = 0
# for j in range(len(pattern)):
# if i+1+(i-j) in range(len(pattern)) and \
    #                      pattern[j] != pattern[i+1+(i-j)]:
# smudges += len([k for k in range(len(pattern[j])) if \
    #                       pattern[j][k] != pattern[i+1+(i-j)][k]])
# if smudges == y:
# return i
# return None
