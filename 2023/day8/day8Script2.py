# -*- coding: utf-8 -*-
from aocd.models import Puzzle
import threading
import math

# Started down the path of threading but ended up abandoning (until next night when I got this working :)

puz = Puzzle(year=2023,day=8)
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

# LRRLL...
directions = data[0]

# AAA = (BBB, CCC)
turnData = data[2:]

def doStuff(counts,idx,turns,inp,directions):
    count = 0
    while count < 100000:
        i = count % len(directions)
        out = turns[inp][directions[i]]
        if out[-1] == 'Z':
            counts.append(count+1)
            break
        count += 1
        inp = out
    counts[idx] = count+1
    #print(counts)

# turns['AAA'] = {'L':'BBB', 'R':'CCC'}
turns = {}
# inTurns = ['AAA',...]
inTurns = []
for line in turnData:
    inTurns.append(line.split(' ')[0])
    turns[line.split(' ')[0]] = {'L':line.split('(')[1].split(',')[0],
                                 'R':line.split(', ')[1].split(')')[0]}

inputs = [x for x in inTurns if x[-1]=='A']
counts = []
threads = []
# Gather up how many turns it takes to go from initial value to end (for each input)
for i,inp in enumerate(inputs):
    count = 0
    threads.append(threading.Thread(target=doStuff,\
                          args=(counts,i,turns,inp,directions)))
    threads[i].start()
    
for i,inp in enumerate(inputs):
    threads[i].join()
    
print(counts)
# LCM not available in python 3.8, so used GCD
temp = 1
for i in counts:
    temp = temp*i // math.gcd(temp,i)

print(temp)
