import fileinput
inputMap = ''.join(fileinput.input(files='./inputs/day8.txt')).split('\n')

map = []
for m in inputMap:
    map.append([*m])

visible = arr = [['0' for i in range(len(map))] for j in range(len(map[0]))]
scenicScore = arr = [[0 for i in range(len(map))] for j in range(len(map[0]))]

for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        north = []
        south = []
        east = []
        west = []

        for n in range(0, i):
            north.append(map[n][j])
        for s in range(i+1, len(map)):
            south.append(map[s][j])
        for w in range(0, j):
            west.append(map[i][w])
        for e in range(j+1, len(map[0])):
            east.append(map[i][e])

        vNorth = north == [] or map[i][j] > max(north)
        vSouth = south == [] or map[i][j] > max(south)
        vWest = west == [] or map[i][j] > max(west)
        vEast = east == [] or map[i][j] > max(east)

        visible[i][j] = str(int(vNorth or vSouth or vWest or vEast))

        nv = []
        sv = []
        ev = []
        wv = []

        for ni in range(i-1, -1, -1):
            nv.append(map[ni][j])
            if map[i][j] <= map[ni][j]:
                break
        for si in range(i+1, len(map)):
            sv.append(map[si][j])
            if map[i][j] <= map[si][j]:
                break
        for wi in range(j-1, -1, -1):
            wv.append(map[i][wi])
            if map[i][j] <= map[i][wi]:
                break
        for ei in range(j+1, len(map[0])):
            ev.append(map[i][ei])
            if map[i][j] <= map[i][ei]:
                break

        scenicScore[i][j] = len(nv) * len(sv)*len(wv)*len(ev)


sum1 = 0
maxScenicScore = 0
for i in range(len(visible)):
    for j in range(len(visible[0])):
        sum1 += int(visible[i][j])
        if scenicScore[i][j] >= maxScenicScore:
            maxScenicScore = scenicScore[i][j]

print(sum1)
print(maxScenicScore)
