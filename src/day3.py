import fileinput
import string

characters = list(string.ascii_lowercase+string.ascii_uppercase)
priority = 1
priorityMap = {}
for char in characters:
    priorityMap[char] = priority
    priority += 1

rucksacks = ''.join(fileinput.input(files='./inputs/day3.txt')).split('\n')
compartments = []
for ruck in rucksacks:
    compartments.append([ruck[0:len(ruck)//2], ruck[len(ruck)//2:]])

scores1 = []
for comp in compartments:
    scores1.append(
        priorityMap[''.join(set(comp[0]).intersection(set(comp[1])))])

print(sum(scores1))

commonItemPriority = []
for group in range(int(len(rucksacks)/3)):
    commonItemPriority.append(priorityMap[''.join(
        set(rucksacks[3*group+0]).intersection(set(rucksacks[3*group+1])).intersection(set(rucksacks[3*group+2])))]
    )
print(sum(commonItemPriority))
