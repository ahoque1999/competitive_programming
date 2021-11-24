n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

a = a[::-1]
counts = [0] * n
counts[0] = 1
unique = [a[0]]

presence = [0] * 10 ** 5
presence[a[0] - 1] = 1

for i in range(1, n):
    if presence[a[i] - 1] == 0:
        presence[a[i] - 1] = 1
        counts[i] = counts[i - 1] + 1
    else:
        counts[i] = counts[i - 1]

counts = counts[::-1]

for i in range(m):
    li = int(input())
    print(counts[li - 1])