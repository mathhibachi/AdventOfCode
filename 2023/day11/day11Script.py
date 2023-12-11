# -*- coding: utf-8 -*-

from aocd.models import Puzzle
# import numpy as np
# import re
# from itertools import count, combinations

puz = Puzzle(year=2023,day=11)
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
data = inData

# nrows = len(data)
# ncols = len(data[0])
# newData = [['' for x in data[0]] for y in data]
# col = {}

newData = []
# Add extra line for any blank lines '....'
for i,line in enumerate(data):
    newData.append(line)
    if '#' not in line:
        newData.append(line)
    # for j,char in enumerate(line):
    #     if not j in col.keys():
    #         col[j] = False
    #     if char=='#':
    #         col[j] = True

#Transpose and repeat
newData = [''.join(s) for s in zip(*newData)]
newerData = []
for i,line in enumerate(newData):
    newerData.append(line)
    if '#' not in line:
        newerData.append(line)

# Transpose back
newerData = [''.join(s) for s in zip(*newerData)]

galaxies = set()
for i in range(len(newerData)):
    for j in range(len(newerData[0])):
        if newerData[i][j]=="#":
            galaxies.add((i,j))

galaxies = list(galaxies)
paths = 0
for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
        paths += abs(galaxies[i][0]-galaxies[j][0]) +\
                 abs(galaxies[i][1]-galaxies[j][1])

#print(data)
#print(newerData)                 
print(paths)

# newestData = []
# counter = count(1)
# for i,line in enumerate(newData):
#     newLine = ''
#     for j in col.keys():
#         if col[j]:
#             newLine += newData[i][j]
#         else:
#             newLine += '..'
#     newLine = re.sub('#',lambda x: str(next(counter)),newLine)
#     newestData.append(newLine)

# numGalaxies = int(re.findall(r'\d',newestData[-1])[-1])


# combs = combinations(range(1,numGalaxies+1),2)
# for c in combs:
#     print(c)
            
#     for j in range(len(line)):
#         if col[j] == False:
#             newestData = line[:j]+'.'+line[j:]
        
# for i,line in enumerate(data):
#     if not line.find('#'):
#         newData.insert(i,line)
