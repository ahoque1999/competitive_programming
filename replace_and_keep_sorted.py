n, q, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.append(k + 1)

permutations = [0] * n
for index in range(1, n - 1):
    permutations[index] = a[index + 1] - a[index - 1] - 2

cumulative_sum = [0] * n
cumulative_sum[0] = 0

for index in range(1, n - 1):
    cumulative_sum[index] = cumulative_sum[index - 1] + permutations[index]

for query in range(q):
    l, r = list(map(int, input().split()))

    if l == r:
        print(k - 1)
        continue

    total = 0

    if l - r != 1:
        total += cumulative_sum[r - 2] -  cumulative_sum[l - 1]
    
    total += a[l] - 2
    total += k + 1 - a[r - 2] - 2

    print(total)