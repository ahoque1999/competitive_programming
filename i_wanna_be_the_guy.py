n = int(input())
x = set(input().split()[1:])
for i in input().split()[1:]:
    x.add(i)
if n == len(x):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
