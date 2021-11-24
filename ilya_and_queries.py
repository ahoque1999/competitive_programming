s = input()

n = len(s)
counts = [0] * n
for i in range(1, n):
    if s[i] == s[i - 1]:
        counts[i] = counts[i - 1] + 1
    else:
        counts[i] = counts[i - 1]

m = int(input())

for i in range(m):
    li, ri = list(map(int, input().split()))
    print(counts[ri - 1] - counts[li - 1])