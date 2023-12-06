# -*- coding: utf-8 -*-

from aocd.models import Puzzle

puz = Puzzle(year=2023,day=6)
# Example input data
exData = puz.example_data.splitlines()
# Full input data
inData = puz.input_data.splitlines()

# Get race durations and distances from input
for i,line in enumerate(inData):
    print(line.split())
    if i == 0:
        raceDurations = [int(x) for x in line.split()[1:]]
    else:
        raceDistances = [int(x) for x in line.split()[1:]]

print(raceDurations,raceDistances)

ways = []
for i,duration in enumerate(raceDurations):
    wins = 0
    for j in range(duration+1):
        # Get distance possible if holding down button for 0 up to duration 
        #   msecs (holding down button for 2 msecs in a 9 msec race leaves
        #   7 msecs * 2mm per msec)
        # If distance possible greater than record, add to win total
        if j*(duration-j)>raceDistances[i]:
            wins += 1
    print(wins)
    # Store number of ways possible to beat record in this race
    ways.append(wins)

# Find product of win totals possible
prod = 1
for wins in ways:
    prod *= wins

# Answer part 1
print(prod)

# Re-store the data for part 2 as strings and concatenate for single race
for i,line in enumerate(inData):
    print(line.split())
    if i == 0:
        raceDurations = [x for x in line.split()[1:]]
    else:
        raceDistances = [x for x in line.split()[1:]]

dur = ''
dist = ''
for i,x in enumerate(raceDurations):
    dur += x
    dist += raceDistances[i]

# Store race duration and distance as int
dur = int(dur)
dist = int(dist)

# Determine number of ways (how long to hold button) to win this longer race
wins = 0
for j in range(dur+1):
    if j*(dur-j)>dist:
        wins += 1
    #print(wins)
    
print(wins)
