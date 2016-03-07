import sys, math

t = int(raw_input().strip())
for a0 in xrange(t):
    myRange = map(int,raw_input().split())
    tot = 0
    lowestRoot = math.ceil(math.sqrt(myRange[0]))
    currN = lowestRoot
    while currN ** 2 <= myRange[1]:
        currN += 1
        tot += 1
    print tot