import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

total = len(arr)
frac_pos = float(sum([1 for i in arr if i > 0])) / total if total != 0 else 0
frac_zero = float(sum([1 for i in arr if i == 0])) / total if total != 0 else 0
frac_neg = float(sum([1 for i in arr if i < 0])) / total if total != 0 else 0
print "%0.6f" % frac_pos
print "%0.6f" % frac_neg
print "%0.6f" % frac_zero