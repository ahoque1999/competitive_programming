n = int(input())
s = list(map(int, input()))
m = list(map(int, input()))

# moriarty
mor_s = sorted(s)
mor_m = sorted(m)

moriarty = 0
for i in range(n):
    number = mor_s[i]
    for j in range(n):
        if mor_m[j] != "used" and mor_m[j] >= number:
            mor_m[j] = "used"
            moriarty += 1
            break

print(n - moriarty)

# sherlock
she_s = sorted(s)
she_m = sorted(m)

sherlock = 0
she_s = she_s[::-1]
for i in range(n):
    if she_s[i] < she_m[-1]:
        sherlock += 1
        she_m.pop(-1)

print(sherlock)