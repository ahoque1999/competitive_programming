n = int(input())
a = list(map(int, input().split()))

counts = [1] * n

for i in range(1, n):
    if a[i] >= a[i - 1]:
        counts[i] = counts[i - 1] + 1

print(max(counts))