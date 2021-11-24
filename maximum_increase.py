n = int(input())
a = list(map(int, input().split()))
maximums = [1] * n
for i in range(1, n):
    if a[i] > a[i - 1]:
        maximums[i] = maximums[i - 1] + 1
print(max(maximums))