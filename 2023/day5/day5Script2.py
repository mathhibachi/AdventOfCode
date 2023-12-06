# -*- coding: utf-8 -*-
from aocd.models import Puzzle

puz = Puzzle(year=2023,day=5)
exData = puz.examples[0].input_data.splitlines()
inData = puz.input_data.splitlines()

exData = [x for x in exData if len(x)>0]
inData = [x for x in inData if len(x)>0]

class plantingMap:
    def __init__(self,name):
        self.name = name
        self.srcStart = []
        self.srcRng = []
        self.dstStart = []
        self.ranges = []
        
        self.inputs = []
        self.outputs = []
        
    def addLine(self,line):
        line = [int(x) for x in line]
        self.srcStart.append(line[1])
        self.srcRng.append(line[2])
        self.dstStart.append(line[0])
        self.ranges.append(range(line[1],line[1]+line[2]))
        
        # for x in range(line[1],line[1]+line[2]):
        #     self.inputs.append(x)
        # for x in range(line[0],line[0]+line[2]):
        #     self.outputs.append(x)
    
    def getOutput(self,inValue):
        out = -1
        for i,start in enumerate(self.srcStart):
            if inValue>=start and inValue<start+self.srcRng[i]:
                out = self.dstStart[i]+(inValue-start)
        if out > -1:
            return out
        else:
            return inValue
        # if inValue in self.inputs:
        #     return self.outputs[self.inputs.index(inValue)]
        # else:
            # return inValue
            
    def splitRanges(self,inRng):
        oldRange = range(0)
        newRange = range(0)
        for i,rng in enumerate(self.ranges):
            if inRng[0] >= rng[0] and inRng[-1] <= rng[-1]:
                # Contained in single range
                print("single range")                
                #outValue = self.getOutput(inRng[0])
                oldRange = range(inRng[0],inRng[0] + (len(inRng)))
                newRange = range(0)
                break
            elif inRng[0] >= rng[0] and inRng[0] <= rng[-1]:
                # Input range is longer, split
                print("longer input range")                
                #outValue = self.getOutput(inRng[0])
                oldRange = range(inRng[0],inRng[0] + rng[-1]-inRng[0])
                newRange = range(rng[-1]+1,inRng[-1]+1)
                break
            
        if len(oldRange) == 0:
            # Not contained in map, return input
            oldRange = inRng
            
        return[oldRange,newRange]
    
    def getRangeOutput(self,inRng):
        outRng = range(0)
        for i,rng in enumerate(self.ranges):
            if inRng[0] >= rng[0] and inRng[-1] <= rng[-1]:
                print('Contained within '+self.name+' range '+str(i))
                outValue = self.getOutput(inRng[0])
                outRng = range(outValue,outValue + (len(inRng)))
                break
            
        if len(outRng) > 0:
            return outRng
        else:
            print('Range not contained within '+self.name)
            return inRng
                            
        
section = ''
allMaps = []
maps = {}
for line in inData:
    line = line.split()
    
    if line[0] == 'seeds:':
        seeds = line[1:]
    elif line[0] == 'seed-to-soil':
        section = 'seed2soil'
        maps[section] = plantingMap(section)
        print(section)
    elif line[0] == 'soil-to-fertilizer':
        section = 'soil2fert'
        maps[section] = plantingMap(section)
        print(section)
    elif line[0] == 'fertilizer-to-water':
        section = 'fert2water'
        maps[section] = plantingMap(section)
        print(section)
    elif line[0] == 'water-to-light':
        section = 'water2light'
        maps[section] = plantingMap(section)
        print(section)
    elif line[0] == 'light-to-temperature':
        section = 'light2temp'
        maps[section] = plantingMap(section)
        print(section)
    elif line[0] == 'temperature-to-humidity':
        section = 'temp2humidity'
        maps[section] = plantingMap(section)
        print(section)
    elif line[0] == 'humidity-to-location':
        section = 'humidity2loc'
        maps[section] = plantingMap(section)
        print(section)
    else:
        print(line)
        maps[section].addLine(line)

for x in maps:
    allMaps.append(maps[x])

seeds = [int(x) for x in seeds]

rngs = []
loc = -1
for i in range(0,len(seeds)-1,2):
    #print(seeds[i])
    rngs.append(range(seeds[i],seeds[i]+seeds[i+1]))

locs = []
newRngs = []
for seedRange in rngs:
    x = seedRange
    for plantMap in allMaps:
        mapComplete = False
        while not mapComplete:            
            temp = plantMap.splitRanges(x)
            if len(temp[1]) == 0:
                x = plantMap.getRangeOutput(temp[0])
                newRngs.append(x)
                mapComplete = True
                break
            else:
                x = plantMap.getRangeOutput(temp[0])
                newRngs.append(x)
                x = temp[1]

print(newRngs)
            
# for seedRange in rngs:
#     x = seedRange
#     for plantMap in allMaps:
#         x = plantMap.getRangeOutput(x)
#     locs.append(x)
        
# print(locs)
print(min([x[0] for x in newRngs]))
