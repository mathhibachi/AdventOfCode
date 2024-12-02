# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from collections import Counter

fin = 'day1Input.txt'

## Part 1
data = pd.read_csv(fin,delimiter='\s+',header=None)
data.columns = ['num1','num2']
num1 = np.sort(np.array([data['num1']]))
num2 = np.sort(np.array([data['num2']]))
diff = np.abs(num1-num2)
#print(diff)
print(f'Total diff: {np.sum(diff)}')

## Part 2

similarities = []
counts = Counter(data['num2'])
for number1 in data['num1']:
    if number1 in counts.keys():
        similarities.append(number1*counts[number1])
    else:
        continue
print(f'Total similarity score: {sum(similarities)}')

