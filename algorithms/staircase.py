import sys


n = int(raw_input().strip())
for x in range(n):
    outStr = ""
    for y in range(n):
        if y >= n-(x+1):
            outStr += "#"
        else:
            outStr += " "
    print outStr