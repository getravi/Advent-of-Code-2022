import fileinput
from copy import deepcopy

input = ''.join(fileinput.input(files='./inputs/day11.txt')).split('\n')
numberOfMonkeys = (len(input)+1)//7
mData = [[] for i in range(numberOfMonkeys)]
m = 0
maxFactor = 1
for i in range(len(input)):
    m = i//7
    if i % 7 == 0 or i % 7 == 6:
        pass
    elif '  Starting items: ' in input[i]:
        s = str.replace(input[i], '  Starting items: ', '')
        mData[m].append(list(map(int, s.split(', '))))
    elif '  Operation: new = ' in input[i]:
        s = str.replace(input[i], '  Operation: new = ', '')
        mData[m].append(s)
    elif '  Test: divisible by ' in input[i]:
        s = str.replace(input[i], '  Test: divisible by ', '')
        mData[m].append(int(s))
        maxFactor *= int(s)
    elif '    If true: throw to monkey ' in input[i]:
        s = str.replace(input[i], '    If true: throw to monkey ', '')
        mData[m].append(int(s))
    elif '    If false: throw to monkey ' in input[i]:
        s = str.replace(input[i], '    If false: throw to monkey ', '')
        mData[m].append(int(s))
    else:
        pass

mData2 = deepcopy(mData)
inspections = [0 for i in range(numberOfMonkeys)]

for round in range(20):
    for i in range(len(mData)):
        for item in mData[i][0]:
            old = item
            inspections[i] += 1
            new = eval(mData[i][1])//3
            test = new % mData[i][2]
            if test == 0:
                mData[mData[i][3]][0].append(new)
            else:
                mData[mData[i][4]][0].append(new)
        mData[i][0] = []


inspections.sort(reverse=True)
print(inspections[0]*inspections[1])


inspections2 = [0 for i in range(numberOfMonkeys)]
for round in range(10000):
    for i in range(numberOfMonkeys):
        if len(mData2[i][0]) == 0:
            continue
        for item in mData2[i][0]:
            old = item
            new = eval(mData2[i][1]) % maxFactor
            test = new % mData2[i][2]
            if test == 0:
                mData2[mData2[i][3]][0].append(new)
            else:
                mData2[mData2[i][4]][0].append(new)
            inspections2[i] += 1
            mData2[i][0] = mData2[i][0][1:]

inspections2.sort(reverse=True)
print(inspections2[0]*inspections2[1])
