# -*- coding: utf-8 -*-

fin = 'day1Input.txt'

linecodes = []

tempHash = {'one':'1',
            'two':'2',
            'three':'3',
            'four':'4',
            'five':'5',
            'six':'6',
            'seven':'7',
            'eight':'8',
            'nine':'9'}

with open(fin) as f:
    for line in f.readlines():
        line = line.strip().lower()
        # print(line.strip())
       
        # From left
        newLine = ''
        for c in line:
            newLine = newLine + c
            for word,num in tempHash.items():
                if word in newLine:
                    newLine = newLine.replace(word,num)
                    
        # From right (reversed)
        newLine2 = ''
        for i in range(len(line),0,-1):
            newLine2 += line[i-1]
            for word,num in tempHash.items():
                if word in newLine2[::-1]:
                    newLine2 = newLine2.replace(word[::-1],num)
       
        # Put reversed line in correct order
        newLine2 = newLine2[::-1]        
        print(newLine,newLine2)
        
        temp = [int(i) for i in newLine if i.isdigit()]
        temp2 = [int(i) for i in newLine2 if i.isdigit()]
        
        print(temp[0],temp2[-1])
        linecodes.append(str(temp[0])+str(temp2[-1]))

codesum = 0
for code in linecodes:
    codesum += int(code)
   
print(codesum)
