from aocd.models import Puzzle
import numpy as np

puz = Puzzle(year=2023,day=14)
# Example input data
exData = puz.example_data.splitlines()
# Full input data
inData = puz.input_data.splitlines()

# If reading in from local file
# exData2 = []
# with open('day13Input2.txt') as f:
#   for line in f.readlines():
#     exData2.append(line.strip())

# Set data set to use for testing
data = exData

stops = {}
for i,line in enumerate(data):
    for j,c in enumerate(line):
        if C=='#':
            stop = [i,j]
