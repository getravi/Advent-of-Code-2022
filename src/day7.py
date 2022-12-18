import fileinput

commands = list(map(lambda a: a.split(' '), ''.join(
    fileinput.input(files='./inputs/day7.txt')).split('\n')))

files = []
currentPath = ['/']

for c in commands:
    match c[0]:
        case '$':
            if c[1] == 'ls':
                next
            elif c[1] == 'cd':
                if c[2] == '/':
                    currentPath = ['/']
                    next
                elif c[2] == '..':
                    currentPath.pop()
                    next
                else:
                    currentPath.append(c[2] + '/')
            else:
                next
        case 'dir':
            next
        case default:
            if currentPath == None:
                currentPath = ['/']
            currentPathString = ''.join(currentPath + [c[1]])
            files.append([currentPath + [c[1]], currentPathString, c[0]])

folders = ['/']
for f in files:
    for i in range(0, len(f[0])):
        if '/'.join(f[0][0:i]) not in folders:
            folders.append(''.join(f[0][0:i]))

filteredFolders = []
for fols in folders:
    if fols not in filteredFolders and fols != '':
        filteredFolders.append(fols)


folderSizes = []
for j in range(0, len(filteredFolders)):
    folderSizes.append([filteredFolders[j], 0])
    for fi in files:
        if filteredFolders[j] in fi[1]:
            folderSizes[j][1] += int(fi[2])

spacetoFree = folderSizes[0][1] - 70000000 + 30000000


print(sum(x[1] for x in
          list(filter(lambda x: x[1] <= 100000, folderSizes))))
print(sorted(
    list(filter(lambda x: x[1] >= spacetoFree, folderSizes)), key=lambda k: k[1])[0][1])
