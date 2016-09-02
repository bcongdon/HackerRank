from collections import defaultdict

n = int(raw_input())
numbers = map(int, raw_input().split(" "))
print round(sum(numbers) / float(n), 1)
numbers.sort()
if len(numbers) % 2 == 0:
    print (numbers[len(numbers) / 2] + numbers[(len(numbers) / 2) - 1]) / 2.0
else:
    print numbers[len(numbers) / 2]
    
counts = defaultdict(int)
for n in numbers:
    counts[n] += 1
max_count = max(counts.values())
print min(x for x in counts if counts[x] == max_count)
