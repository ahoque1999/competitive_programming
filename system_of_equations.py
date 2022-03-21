m, n = list(map(int, input().split()))

counter = 0

for a in range(m + 1):
    for b in range(n + 1):
        if a ** 2 + b == m and b ** 2 + a == n:
            counter += 1

print(counter)
