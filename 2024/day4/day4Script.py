# -*- coding: utf-8 -*-

fin = 'day4Input.txt'
fin2 = 'day4SampleInput.txt'

def checkLeft(stuff,row,col):
    if col<3:
        return False
    else:
        if stuff[row][col-3:col] == 'SAM':
            return True
        else:
            return False
        
def checkRight(stuff,row,col):
    if col>len(stuff[0])-4:
        return False
    else:
        if stuff[row][col+1:col+4] == 'MAS':
            return True
        else:
            return False
        
def checkUp(stuff,row,col):
    if row<3:
        return False
    else:
        if stuff[row-1][col] == 'M' and stuff[row-2][col] == 'A' and\
                                    stuff[row-3][col] == 'S':
            return True
        else:
            return False
        
def checkDown(stuff,row,col):
    if row>len(stuff)-4:
        return False
    else:
        if stuff[row+1][col] == 'M' and stuff[row+2][col] == 'A' and\
                                    stuff[row+3][col] == 'S':
            return True
        else:
            return False

def checkLeftDiagUp(stuff,row,col):
    if row<3 or col<3:
        return False
    else:
        if stuff[row-1][col-1] == 'M' and stuff[row-2][col-2] == 'A' and\
                                    stuff[row-3][col-3] == 'S':
            return True
        else:
            return False

def checkLeftDiagDown(stuff,row,col):
    if row>len(stuff)-4 or col<3:
        return False
    else:
        if stuff[row+1][col-1] == 'M' and stuff[row+2][col-2] == 'A' and\
                                    stuff[row+3][col-3] == 'S':
            return True
        else:
            return False

def checkRightDiagUp(stuff,row,col):
    if row<3 or col>len(stuff[0])-4:
        return False
    else:
        if stuff[row-1][col+1] == 'M' and stuff[row-2][col+2] == 'A' and\
                                    stuff[row-3][col+3] == 'S':
            return True
        else:
            return False

def checkRightDiagDown(stuff,row,col):
    if row>len(stuff)-4 or col>len(stuff[0])-4:
        return False
    else:
        if stuff[row+1][col+1] == 'M' and stuff[row+2][col+2] == 'A' and\
                                    stuff[row+3][col+3] == 'S':
            return True
        else:
            return False

def checkForWord(stuff,row,col):
    wordSum = 0    
    if checkRight(stuff,row,col):
        # print(['RightTrue',row,line])
        wordSum += 1
    if checkLeft(stuff,row,col):
        # print(['LeftTrue',row,line])
        wordSum += 1
    if checkUp(stuff,row,col):
        # print(['UpTrue',row,line])
        wordSum += 1
    if checkDown(stuff,row,col):
        # print(['DownTrue',row,line])
        wordSum += 1
    if checkRightDiagDown(stuff,row,col):
        # print(['RightDownTrue',row,col]) 
        wordSum += 1               
    if checkRightDiagUp(stuff,row,col):
        # print(['RightUpTrue',row,col])
        wordSum += 1
    if checkLeftDiagDown(stuff,row,col):
        # print(['LeftDownTrue',row,col]) 
        wordSum += 1               
    if checkLeftDiagUp(stuff,row,col):
        # print(['LeftUpTrue',row,col])
        wordSum += 1
        
    return wordSum
  
def checkMAS(stuff,row,col):
    if col>len(stuff[0])-3 or row>len(stuff)-3:
        return False
    if not stuff[row+1][col+1]=='A':
        return False
    if stuff[row][col] == 'S' and not stuff[row+2][col+2] == 'M':
        return False
    if stuff[row][col] == 'M' and not stuff[row+2][col+2] == 'S':
        return False
    if stuff[row][col+2] == 'M' and stuff[row+2][col] == 'S':
        return True
    if stuff[row][col+2] == 'S' and stuff[row+2][col] == 'M':
        return True
    return False  

## Part 1
numSum = 0
stuff = []
with open(fin) as f:
    for line in f.readlines():
        stuff.append(line.strip())
    for row,line in enumerate(stuff):
        for col,x in enumerate(line):
            if x == 'X':
                numSum += checkForWord(stuff,row,col)
print(f'Number of xmas: {numSum}')

## Part 2
numSum = 0
stuff = []
with open(fin2) as f:
    for line in f.readlines():
        stuff.append(line.strip())
    for row,line in enumerate(stuff):
        for col,x in enumerate(line):
            if x == 'M' or x == 'S':
                if checkMAS(stuff,row,col):
                    numSum += 1

print(f'Number of MAS: {numSum}')
