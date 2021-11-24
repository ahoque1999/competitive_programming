for i in range(int(input())):
    n, m, x = list(map(int, input().split()))
    a, b = [n, x // n] if x % n == 0 else [x % n, x // n + 1]
    print(m * (a - 1) + b)
