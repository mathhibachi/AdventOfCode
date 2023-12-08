# -*- coding: utf-8 -*-

from aocd.models import Puzzle
import threading

# Started down the path of threading but ended up abandoning

def runStuff():
    
    puz = Puzzle(year=2023,day=8)
    # Example input data
    exData = puz.example_data.splitlines()
    # Full input data
    inData = puz.input_data.splitlines()
    
    exData2 = []
    with open('day8Input3.txt') as f:
      for line in f.readlines():
          exData2.append(line.strip())
    
    data = inData
    directions = data[0]
    
    turnData = data[2:]
    
    turns = {}
    inTurns = []
    outTurns = {'L':[],'R':[]}
    for line in turnData:
        inTurns.append(line.split(' ')[0])
        outTurns['L'].append(line.split('(')[1].split(',')[0])
        turns[line.split(' ')[0]] = {'L':line.split('(')[1].split(',')[0],
                                     'R':line.split(', ')[1].split(')')[0]}
    
    inputs = [x for x in inTurns if x[-1]=='A']
    count = 0
    
    i = count % len(directions)
    
    t = [None]*len(inputs)
    results = [None]*len(inputs)
    for i in range(len(threads)):
        t[i] = threading.Thread(target=findPaths, 
                          args=(inputs[0],directions[i],turns,results,i))
        
        t[i].start()
        
    for i in range(len(threads)):
        t[i].join()
    
    print(results)

def findPaths(inp,direction,turns,result,idx):
    out = turns[inp][direction]
    if out[-1] == 'Z':
        result[idx] = True
    else:
        result[idx] = False
    inp = out
    return out        
     
    # temp = [x for x in outs if x[-1]=='Z']
    #         if len(temp) == len(outs):
    #             print('Made it in '+str(count+1)+' turns')
    #             break
            # count += 1
            # inputs = outs

if __name__=="__main__":
    runStuff()
    
    
    
#print(turns)
#inp = inTurns[0]
#inp = 'AAA'
# count = 0
# while count<1000000:
#     i = count % len(directions)
#     #print(i)
#     if inp in inTurns:
#         out = turns[inp][directions[i]]
#     else:
#         print('Not a valid input')
#         break
#     #print(inp,out)
#     if out=='ZZZ':
#         print('Made it in '+str(count+1)+' turns')
#         break
#     count += 1
#     inp = out
    
# re.find   
