t = int(raw_input().strip())
for x in range(t):
    string = raw_input()
    c = 1
    prev = string[0]
    deletions = 0
    while c < len(string):
        if string[c] == prev:
            deletions += 1
        else:
            prev = string[c]
        c +=1
    print deletions