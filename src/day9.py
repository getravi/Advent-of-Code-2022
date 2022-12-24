import fileinput
import math
from copy import deepcopy

moves = list(map(lambda x: x.split(' '), ''.join(
    fileinput.input(files='./inputs/day9.txt')).split('\n')))


def updateKnot(leader, follower):
    # Update Tail position
    # check if Head and Tail are at most one position away
    if abs(leader[0] - follower[0]) <= 1 and abs(leader[1] - follower[1]) <= 1:
        follower = follower
    # Check if tail is in the same row as head
    elif follower[0] == leader[0] and abs(leader[1] - follower[1]) == 2:
        follower[1] = follower[1] + \
            int(math.copysign(1, (leader[1] - follower[1])))
    # Check if tail is in the same column as head
    elif follower[1] == leader[1] and abs(leader[0] - follower[0]) == 2:
        follower[0] = follower[0] + \
            int(math.copysign(1, (leader[0] - follower[0])))
    # check if diagonal move is needed
    elif follower[0] != leader[0] and follower[1] != leader[1] and (abs(leader[0] - follower[0]) > 1 or abs(leader[1] - follower[1]) > 1):
        follower[0] = follower[0] + \
            int(math.copysign(1, (leader[0] - follower[0])))
        follower[1] = follower[1] + \
            int(math.copysign(1, (leader[1] - follower[1])))
    else:
        follower = follower
    return follower


H = [0, 0]
Knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
KnotsHistory = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                 [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
for m in moves:
    for step in range(1, (int(m[1])+1)):

        # update Head position for each move
        match m[0]:
            case 'U':
                H[1] = H[1] + 1
            case 'D':
                H[1] = H[1] - 1
            case 'R':
                H[0] = H[0] + 1
            case 'L':
                H[0] = H[0] - 1
            case default:
                pass
        '''
        
        # Update Tail position
        # check if Head and Tail are at most one position away
        if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
            T = T
        # Check if tail is in the same row as head
        elif T[0] == H[0] and abs(H[1] - T[1]) == 2:
            T[1] = T[1] + int(math.copysign(1, (H[1] - T[1])))
        # Check if tail is in the same column as head
        elif T[1] == H[1] and abs(H[0] - T[0]) == 2:
            T[0] = T[0] + int(math.copysign(1, (H[0] - T[0])))
        # check if diagonal move is needed
        elif T[0] != H[0] and T[1] != H[1] and (abs(H[0] - T[0]) > 1 or abs(H[1] - T[1]) > 1):
            T[0] = T[0] + int(math.copysign(1, (H[0] - T[0])))
            T[1] = T[1] + int(math.copysign(1, (H[1] - T[1])))
        else:
            T = T
        '''
        for k in range(0, len(Knots)):
            if k == 0:
                Knots[k] = updateKnot(H, Knots[k])
            else:
                Knots[k] = updateKnot(Knots[k-1], Knots[k])
        KnotsHistory.append(deepcopy(Knots))


k1 = [[0, 0]]
k9 = [[0, 0]]
for kh in KnotsHistory:
    if kh[0] not in k1:
        k1.append([*kh[0]])
    if kh[8] not in k9:
        k9.append([*kh[8]])

print(len(k1))
print(len(k9))
