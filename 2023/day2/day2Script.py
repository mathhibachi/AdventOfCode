# -*- coding: utf-8 -*-

import re

fin = 'day2Input.txt'

gameNumSum = 0
powerSum = 0

with open(fin) as f:
    for line in f.readlines():
        gameNum = line.split(' ')[1].split(':')[0]
        tries = line.split(':')[1]
        numTries = len(tries.split(';'))
        status = True
        minRed = 0
        minGreen = 0
        minBlue = 0
        for attempt in tries.split(';'):
            tempRed = re.findall(r'\d+ red',attempt)
            if len(tempRed) > 0:
                tempRed = tempRed[0].split(' ')[0]
                minRed = max(minRed,int(tempRed))
                if int(tempRed)>12:
                    status = False
            tempGreen = re.findall(r'\d+ green',attempt)
            if len(tempGreen) > 0:
                tempGreen = tempGreen[0].split(' ')[0]
                minGreen = max(minGreen,int(tempGreen))
                if int(tempGreen)>13:
                    status = False
            tempBlue = re.findall(r'\d+ blue',attempt)
            if len(tempBlue) > 0:
                tempBlue = tempBlue[0].split(' ')[0]
                minBlue = max(minBlue,int(tempBlue))
                if int(tempBlue)>14:
                    status = False
        if status:
            gameNumSum += int(gameNum)
        
        if minRed == 0:
            minRed = 1
        if minGreen == 0:
            minGreen = 1
        if minBlue == 0:
            minBlue = 1
            
        gamePower = minRed*minBlue*minGreen
        powerSum += gamePower
        print(line)
        print(gamePower)
        print(powerSum)
        
        #print(gameNumSum)
        
        # print(tries,numTries)
        # temp = re.findall(r'\d+ blue',line)
        # print(temp)
        
        
