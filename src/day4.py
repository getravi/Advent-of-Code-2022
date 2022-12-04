import fileinput
import re

pairs = ''.join(fileinput.input(files='./inputs/day4.txt')).split('\n')
full = []
partial = []
for pair in pairs:
    rangeBs = list(map(int, re.split('-|,', pair)))
    isOverlap = rangeBs[0] in range(rangeBs[2], rangeBs[3]+1) or rangeBs[1] in range(
        rangeBs[2], rangeBs[3]+1) or rangeBs[2] in range(rangeBs[0], rangeBs[1]+1) or rangeBs[3] in range(rangeBs[0], rangeBs[1]+1)

    isFullOverlap = (rangeBs[0] >= rangeBs[2] and rangeBs[1] <= rangeBs[3]) or (
        rangeBs[2] >= rangeBs[0] and rangeBs[3] <= rangeBs[1])
    full.append(int(isFullOverlap))
    partial.append(int(isOverlap))

print(sum(full))
print(sum(partial))
