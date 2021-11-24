NUMBERS = 45
n = int(input())

sums = [0] * NUMBERS
sums[0] = 1
for i in range(1, NUMBERS):
    sums[i] = sums[i - 1] + i + 1
    if n < sums[i]:
        print(i)
        for j in range(i - 1):
            print(j + 1, end=" ")
        print(n - sums[i - 2])
        break