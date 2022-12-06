signal = open("./inputs/day6.txt").read()

#define a function to accept a string with 4 characters and return whether all the characters are unique or not
def isUnique(a):
    l = len(a)
    fsum=0
    for x in range(l):
        fsum += a.count(a[x])
    return fsum == l

#Part 1
for i in range(len(signal)-3):
    if isUnique(signal[i:i+4]):       
        print (i+4)
        break

#Part 2
for j in range(len(signal)-13):
    if isUnique(signal[j:j+14]):       
        print (j+14)
        break
        


