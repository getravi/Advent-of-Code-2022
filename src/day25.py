import fileinput

numbers = ''.join(fileinput.input(files='./inputs/day25.txt')).split('\n')
digitMap = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
reverseDigitMap = {2: '2', 1: '1', 0: '0',  -1: '-', -2: '='}


def addSnafu(a, b):
    maxDigits = max(len(a), len(b))
    a = ''.join(list(reversed('0'*(maxDigits - len(a)) + a)))
    b = ''.join(list(reversed('0'*(maxDigits - len(b)) + b)))
    sum = ''
    carry = 0
    for i in range(maxDigits):
        s = digitMap[a[i]] + digitMap[b[i]] + carry
        if s > 2:
            carry = 1
            sum += reverseDigitMap[s-5]
        elif s < -2:
            carry = -1
            sum += reverseDigitMap[s+5]
        else:
            carry = 0
            sum += reverseDigitMap[s]
    if carry != 0:
        sum += reverseDigitMap[carry]
    return ''.join(list(reversed(sum)))


snafuSum = '0'
for n in numbers:
    snafuSum = addSnafu(snafuSum, n)

print(snafuSum)
