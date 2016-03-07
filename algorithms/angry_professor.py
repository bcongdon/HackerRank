import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    onTime = sum(1 for x in a if x <= 0)
    print "YES" if onTime < k else "NO"