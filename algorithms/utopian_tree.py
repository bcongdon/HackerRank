#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    h = 1
    for x in range(n):
        if x % 2 == 0:
            h *= 2
        else:
            h += 1
    print h
            