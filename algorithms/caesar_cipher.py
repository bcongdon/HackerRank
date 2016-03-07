import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
out = ""
while k > 26:
    k -= 26
for ch in s:
    if (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122):
        newChNum = ord(ch) + k
        if ch.isupper():
            if newChNum > ord('Z'):
                newChNum -= 26
            elif newChNum < ord('A'):
                newChNum += 26
        else:
            if newChNum > ord('z'):
                newChNum -= 26
            elif newChNum < ord('a'):
                newChNum += 26
        out += chr(newChNum)
    else:
        out += ch
print out