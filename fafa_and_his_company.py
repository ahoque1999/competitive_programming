n = int(input())
print(sum([1 for i in range(1, n // 2 + 1) if (n - i) % i == 0]))