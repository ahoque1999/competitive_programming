n = int(input())
s = input()

z = sum([1 for char in s if char == "z"])
n = sum([1 for char in s if char == "n"])

for i in range(n):
    print("1", end=" ")
for i in range(z):
    print("0", end=" ")
print()