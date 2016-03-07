from __future__ import print_function

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.reverse()
for x in arr:
    print(x,end =" ")