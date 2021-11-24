n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

length = n - k + 1
sums = [0] * length
sums[0] = sum(h[:k])
for i in range(1, length):
    sums[i] = sums[i - 1] - h[i - 1] + h[i - 1 + k]

print(sums.index(min(sums)) + 1)