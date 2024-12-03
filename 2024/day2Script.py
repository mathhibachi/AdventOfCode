# -*- coding: utf-8 -*-

fin = 'day2Input.txt'

def checkLine(line):
    if sorted(line)==line or sorted(line,reverse=True)==line:
            diffs = [abs(j-i) for i, j in zip(line[:-1], line[1:])]
            if min(diffs)>0 and max(diffs) <= 3:
                return True

## Part 1
count = 0
with open(fin) as f:
    for line in f.readlines():
        line = [float(x) for x in line.strip().split()]
        #print(line)
        if checkLine(line):
            count += 1
print(f'Number of safe lines: {count}')
    
## Part 2
count = 0
with open(fin) as f:
    for line in f.readlines():
        line = [float(x) for x in line.strip().split()]
        if checkLine(line):
            count += 1
        else:
            for i,x in enumerate(line):
                newLine = line[:i]+line[i+1:]
                if checkLine(newLine):
                    count += 1
                    break
print(f'Number of safe lines: {count}')

