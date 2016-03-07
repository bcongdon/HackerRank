#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    digits = [int(i) for i in str(n)]
    print sum(1 for i in digits if i != 0 and n % i == 0)