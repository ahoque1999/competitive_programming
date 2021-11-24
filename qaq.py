s = input()

convert = ""
for char in s:
    if char == "Q":
        convert += "1"
    elif char == "A":
        convert += "2"

n = len(convert)

branches = [0] * n

for i in range(n):
    if convert[i] == "1":
        branches[i] = [i for i in range(i, n) if convert[i] == "2"]

for i in range(n):
    if convert[i] == "2":
        branches[i] = sum([1 for i in range(i, n) if convert[i] == "1"])

sum = 0
for i in range(n):
    if convert[i] == "1":
        for branch in branches[i]:
            sum += branches[branch]
            
print(sum)