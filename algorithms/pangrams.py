input_str = raw_input().lower().strip()

letters = set()

for x in input_str:
    if x != ' ':
        letters.add(x)
    
if len(letters) >= 26:
    print "pangram"
else:
    print "not pangram"