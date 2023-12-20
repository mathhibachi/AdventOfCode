# -*- coding: utf-8 -*-
from aocd.models import Puzzle

puz = Puzzle(year=2023,day=18)
# Example input data
#exData = puz.example_data.splitlines()
exData = puz.examples[0].input_data.splitlines()
# Full input data
inData = puz.input_data.splitlines()

dirMap = {0:'R', 1:'D', 2:'L', 3:'U'}
# If reading in from local file
# exData2 = []
# with open('day13Input2.txt') as f:
#   for line in f.readlines():
#     exData2.append(line.strip())

# Set data set to use for testing
data = inData

#print(data)

# Used in calculating area while traversing coordinates
def getInfo(coord1,coord2):
    return (coord1[0]*coord2[1] - coord1[1]*coord2[0])

# Stores 'colors' from input
colors = []
# Stores directions from input as tuples (example: ('R',4))
oldDirections = []

for line in data:
    line = line.split(' ')
    oldDirections.append((line[0],int(line[1])))
    colors.append(line[2])

# Used in part 2 to stores directions (now based on 'color' codes)
newDirections = [(dirMap[int(x[-2])],int(x[2:-2],16)) for x in colors]    

# Stores locations as coordinate pairs (x,y)
coords = [(0,0)]
prevDir = ''
nextDir = ''
xtra = 0

directions = newDirections

for i,loc in enumerate(directions):
    if i == len(directions)-1:
        nextDir = directions[0][0]
    else:
        nextDir = directions[i+1][0]
        
    if loc[0] == 'R':
        # Turning clockwise
        if prevDir == 'U' and nextDir == 'D':
            xtra = 1
        # Turning counter-clockwise
        elif prevDir == 'D' and nextDir == 'U':
            xtra = -1
        else:
            xtra = 0
        coords.append((coords[-1][0]+loc[1] + xtra,coords[-1][1]))
    elif loc[0] == 'L':
        if prevDir == 'D' and nextDir == 'U':
            xtra = 1
        elif prevDir == 'U' and nextDir == 'D':
            xtra = -1
        else:
            xtra = 0
        coords.append((coords[-1][0]-loc[1] - xtra,coords[-1][1]))
    elif loc[0] == 'D':
        if prevDir == 'R' and nextDir == 'L':
            xtra = 1
        elif prevDir == 'L' and nextDir == 'R':
            xtra = -1
        else:
            xtra = 0
        coords.append((coords[-1][0],coords[-1][1]+loc[1] + xtra))
    elif loc[0] == 'U':
        if prevDir == 'L' and nextDir == 'R':
            xtra = 1
        elif prevDir == 'R' and nextDir == 'L':
            xtra = -1
        else:
            xtra = 0
        coords.append((coords[-1][0],coords[-1][1]-loc[1] - xtra))
    prevDir = loc[0]

# Get area by traversing the coordinate pairs
area = 0
for i in range(len(coords)-1):
    area += getInfo(coords[i],coords[i+1])
area += getInfo(coords[-1],coords[0])
area = abs(area)/2
print(area)

