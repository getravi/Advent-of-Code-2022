import fileinput

program = list(map(lambda x: x.split(' '), ''.join(
    fileinput.input(files='./inputs/day10.txt')).split('\n')))

X = [1]

for p in program:
    if p[0] == 'noop':
        X.append(X[-1])
    else:
        X.append(X[-1])
        X.append(X[-1]+int(p[1]))

sum1 = 20*X[19]+60*X[59]+100*X[99] + 140 * X[139] + 180*X[179] + 220 * X[219]
print(sum1)


for i in range(6):
    line = ''
    for j in range(40):
        pixelPosition = 40*i + j
        if abs(j - X[pixelPosition]) <= 1:
            line += '#'
        else:
            line += '.'
    print(line)
