s = input()
t = input()

pos = 0

for ins in t:
    if ins == s[pos]:
        pos += 1

print(pos + 1)