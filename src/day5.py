import fileinput
import re

#pairs = ''.join(fileinput.input(files='./inputs/day5.txt')).split('\n')

stacksOriginal = []
moves = []
for line in fileinput.input(['./inputs/day5.txt']):
  if  fileinput.lineno() < 9:
    row = []
    for i in range(1, len(line), 4):
        row.append(line[i]) 
    stacksOriginal.append(row)
  elif fileinput.lineno() == 9 or fileinput.lineno() == 10:
    pass
  else:
    moveString =line.split()
    moves.append([int(moveString[1]) , int(moveString[3]) , int(moveString[5])])

i=0
j=0
stacks =[]
for i in range(0,9):
    stack = ''
    for j in range(7,-1,-1):
        stack += stacksOriginal[j][i]
    stacks.append(stack.strip())    

print(stacks)

stacks1 = [*stacks]
stacks2 = [*stacks]

print(stacks1)
print(stacks2)


for m in moves:
    for i in range (0,m[0]):
        x = stacks1[m[1]-1]
        y = x[-1:]
        stacks1[m[1]-1] = x[0:-1]
        stacks1[m[2]-1] = stacks1[m[2]-1] + y

for m in moves:
    x = stacks2[m[1]-1]
    y = x[-m[0]:]
    stacks2[m[1]-1] = x[0:-m[0]]
    stacks2[m[2]-1] = stacks2[m[2]-1] + y

print("---")
"""
print(stacks1)
print(stacks2)

"""
print(''.join(map(lambda n: n[-1:] , stacks1)))
print(''.join(map(lambda n: n[-1:] , stacks2)))

