import fileinput
from ast import literal_eval

input = ''.join(fileinput.input(files='./inputs/day13.txt')).split('\n')
entries = (len(input)+1)//3
left = []
right = []
for i in range(0, len(input), 3):
    left.append(literal_eval(input[i]))
    right.append(literal_eval(input[i+1]))


def compare(a, b):
    items = max(len(a), len(b))
    for i in range(items):
        if type(a[i]) == int and type(b[i]) == int:
            if a[i] < b[i]:
                return True
                break
            elif a[i] > b[i]:
                return False
                break
            else:
                continue
        elif type(a) == int and type(b) != int:
            compare([a], b)
        elif type(a) != int and type(b) == int:
            compare(a, [b])
        else:
            compare(a, b)


results = [False for _ in range(len(left))]
for n in range(len(left)):
    results[n] = compare(left[1], right[1])

print(results)
