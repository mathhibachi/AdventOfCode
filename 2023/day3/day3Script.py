# -*- coding: utf-8 -*-
from aocd.models import Puzzle
#from aocd import get_data
import re

#data = get_data(day=3, year=2023).splitlines()

temp = Puzzle(year=2023, day=3)
data = temp.examples[0].input_data.splitlines()
data = temp.input_data.splitlines()

nums = ['0','1','2','3','4','5','6','7','8','9','.']
chars = []

# Get list of special characters from data set
for line in data:
    for x in line:
        if x not in nums and x not in chars:
            chars.append(x)

#print(chars)

def checkAdj(line,startIdx,endIdx):
    if startIdx>0:
        # print(line[startIdx-1:endIdx+1])
        if line[startIdx-1] in chars:
            return True
        if endIdx < len(line):
            if line[endIdx] in chars:
                return True
    else:
        # print(line[startIdx:endIdx+1])
        if endIdx < len(line):
            if line[endIdx] in chars:
                return True
    return False

def checkOtherRows(line,startIdx,endIdx,prevLine,nextLine):
    if len(prevLine) > 0:
        if startIdx>0:
            for y in prevLine[startIdx-1:endIdx+1]:
                if y in chars:
                    return True
        else:
            for y in prevLine[startIdx:endIdx+1]:
                if y in chars:
                    return True
    if len(nextLine) > 0:
        if startIdx>0:
            for y in nextLine[startIdx-1:endIdx+1]:
                if y in chars:
                    return True
        else:
            for y in nextLine[startIdx:endIdx+1]:
                if y in chars:
                    return True
    return False

prevRow = ''
nextRow = ''
partNums = []
for row,line in enumerate(data):
    if row>0:
        prevRow = data[row-1]
    if row<len(data)-1:
        nextRow = data[row+1]
    #line = '123..56...*23'
    #print(line)
    temp = re.findall('\d+',line)
    temp2 = [(m.start(0),m.end(0)) for m in re.finditer('\d+',line)]
    if len(temp2)>0:
        #print(prevRow)
        #print(line)
        #print(nextRow)
        #print(temp2)
        #print(re.search(temp[0],line).start(),re.search(temp[0],line).end())
        for x in temp2:
            partFlag = False
            startIdx = x[0]
            endIdx = x[1]
            #startIdx = re.search(x,line).start()
            #endIdx = re.search(x,line).end()
            adjFlag = checkAdj(line,startIdx,endIdx)
            prevFlag = checkOtherRows(line,startIdx,endIdx,prevRow,nextRow)
            if adjFlag:
                partNums.append(line[startIdx:endIdx])
            if prevFlag:
                partNums.append(line[startIdx:endIdx])
                
            #print(adjFlag)
    # else:
    #     print(line)
        
    prevRow = ''
    nextRow = ''
    
thing = [int(x) for x in partNums]
print(sum(thing))
