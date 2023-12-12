# -*- coding: utf-8 -*-

from aocd.models import Puzzle
import re

puz = Puzzle(year=2023,day=12)
# Example input data
exData = puz.example_data.splitlines()
# Full input data
inData = puz.input_data.splitlines()

# If reading in from local file
exData2 = []
with open('day12Input2.txt') as f:
  for line in f.readlines():
    exData2.append(line.strip())

# Set data set to use for testing
data = exData2

#print(data)
for line in data:
    pattern, seq = line.split()
    seq = tuple(map(int,seq.split(',')))
    print(pattern,seq)
    
