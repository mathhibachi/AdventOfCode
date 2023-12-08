# -*- coding: utf-8 -*-

from aocd.models import Puzzle
import math

puz = Puzzle(year=2023,day=8)
# Example input data
exData = puz.example_data.splitlines()
# Full input data
inData = puz.input_data.splitlines()

exData2 = []
with open('day8Input3.txt') as f:
  for line in f.readlines():
      exData2.append(line.strip())

data = inData
directions = data[0]

turnData = data[2:]

turns = {}
inTurns = []
outTurns = {'L':[],'R':[]}
for line in turnData:
    inTurns.append(line.split(' ')[0])
    outTurns['L'].append(line.split('(')[1].split(',')[0])
    turns[line.split(' ')[0]] = {'L':line.split('(')[1].split(',')[0],
                                 'R':line.split(', ')[1].split(')')[0]}

inputs = [x for x in inTurns if x[-1]=='A']
counts = []
for inp in inputs:
    count = 0
    while count < 100000:
        i = count % len(directions)
        out = turns[inp][directions[i]]
        if out[-1] == 'Z':
            counts.append(count+1)
            break
        count += 1
        inp = out
    print(counts)

# LCM not available in python 3.8, so used GCD
temp = 1
for i in counts:
    temp = temp*i // math.gcd(temp,i)

print(temp)

