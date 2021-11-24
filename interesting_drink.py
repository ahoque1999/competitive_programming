n = int(input())
x = sorted(list(map(int, input().split())))
q = int(input())

max_cost = max(x)

counts = [0] * (max_cost + 1)

for i in range(n):
    counts[x[i]] = i + 1

for i in range(1, max_cost):
    if counts[i] == 0:
        counts[i] = counts[i - 1]

for i in range(q):
    mi = int(input())

    print(counts[min(mi, max_cost)])