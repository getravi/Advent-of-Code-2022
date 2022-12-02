fileobj = open("./inputs/day1.txt")
lines = fileobj.read().split('\n')
elfNum = 0
data = []
index = 0
for line in lines:
    if line == "":
        calorie = 0
        elfNum += 1
    else:
        calorie = int(line)
    data.append([elfNum, calorie])

# Create a dictionary grouped by Name
d = {}
for row in data:

    # Add name to dict if not exists
    if row[0] not in d:
        d[row[0]] = []

# Add all non-Name attributes as a new list
    d[row[0]].append(row[1])

# Create a dictionary grouped by Name
d2 = dict((k, []) for k, v in d.items())
for elf in d:
    calorieSum = 0
    for num in d[elf]:
        calorieSum += num
    d2[elf].append(calorieSum)

output = sorted(d2.items(), key=lambda item: item[1], reverse=True)[:3]
calSum = 0
for top in output:
    calSum += int(top[1][0])
    print(top)
print(calSum)
