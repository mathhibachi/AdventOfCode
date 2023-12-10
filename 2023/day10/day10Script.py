# -*- coding: utf-8 -*-

from aocd.models import Puzzle

puz = Puzzle(year=2023,day=10)
# Example input data
exData = puz.example_data.splitlines()
# Full input data
inData = puz.input_data.splitlines()

# If reading in from local file
exData2 = []
with open('day10Input3.txt') as f:
  for line in f.readlines():
      exData2.append(line.strip())

data = inData

def move(newData,data,rows,cols,idx):
  # done = False
  # while done==False:
  
    if idx[0]<rows-1:
        # Look down
        if data[idx[0]+1][idx[1]] in ['|','L','J'] and \
          newData[idx[0]+1][idx[1]]<0:
            newData[idx[0]+1][idx[1]] = newData[idx[0]][idx[1]] + 1
    if idx[0]>0 and idx[0]<rows:
        # Look up
        if data[idx[0]-1][idx[1]] in ['|','7','F'] and \
          newData[idx[0]-1][idx[1]]<0:
            newData[idx[0]-1][idx[1]] = newData[idx[0]][idx[1]] + 1
    if idx[1]<cols-1:
        # Look right
        if data[idx[0]][idx[1]+1] in ['-','7','J'] and \
          newData[idx[0]][idx[1]+1]<0:
            newData[idx[0]][idx[1]+1] = newData[idx[0]][idx[1]] + 1
    if idx[1]>0 and idx[1]<cols:
        # Look left
        if data[idx[0]][idx[1]-1] in ['-','L','F'] and \
          newData[idx[0]][idx[1]-1]<0:
            newData[idx[0]][idx[1]-1] = newData[idx[0]][idx[1]] + 1
    return newData
            
                
# def completeRow(row,colNum):
#     newRow = [-1 for x in row]
#     newRow[colNum] = 0
#     if colNum>0:
#         colIdx = colNum-1
#         while colIdx >=0:
#             if row[colIdx]=='-' and newRow[colIdx+1]>=0:
#                 newRow[colIdx] = newRow[colIdx+1] + 1
#             #if row[colIdx]=='F'
#             colIdx -= 1
#     print(row)
#     print(newRow) 

newData = []
rows = 0
for i,line in enumerate(data):
    rows += 1
    newData.append([-1 for x in line])
    if 'S' in line:
        idx = [i,line.index('S')]

newData[idx[0]][idx[1]] = 0
cols = len(newData[0])

#[print(line) for line in data]

count = 0
done = False
while not done:
    found = False
    for i,line in enumerate(newData):
        if count in line:
            for j,num in enumerate(line):
                if num == count:
                    found = True
                    newData = move(newData,data,rows,cols,[i,j])
    
    if found:
        count += 1
    else:
        done = True
                    

#[print(line) for line in newData]
print(max([max(line) for line in newData]))
    
# newData=move(newData,data,rows,cols,idx)
# [print(line) for line in newData]

# completeRow(data[3],4)
# print([rows,cols],idx)
