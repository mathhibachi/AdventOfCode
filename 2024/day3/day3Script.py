# -*- coding: utf-8 -*-
import re

fin = 'day3Input.txt'
fin2 = 'day3SampleInput2.txt'

def mul(num1,num2):
    return num1*num2

## Part 1
numSum = 0
with open(fin) as f:
    for line in f.readlines():
        stuff = re.findall('mul\(\d+,\d+\)',line)
        for thing in stuff:
            num1=float(thing.split('(')[1].split(',')[0])
            num2=float(thing.split(',')[1].split(')')[0])
            numSum = numSum + mul(num1,num2)
print(f'Sum of mul statements: {numSum}')
    
## Part 2

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern,open(fin).read())

newSum = 0
flag = True
for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag = False
    else:
        if flag:
            x,y = map(int, match[4:-1].split(","))
            newSum += x*y
            
print(f'Sum of revised mul statements: {newSum}')
        

