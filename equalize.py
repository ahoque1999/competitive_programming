n = int(input())
a = input()
b = input()

total = 0

for index in range(n):
    if a[index] != b[index]:
        total += 1

range_iter = iter(range(n - 1))

for index in range_iter:
    if a[index] != b[index] and a[index] != a[index + 1] and a[index + 1] != b[index + 1]:
        total -= 1
        next(range_iter, None)

print(total)