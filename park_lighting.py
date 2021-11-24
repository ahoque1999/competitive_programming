for i in range(int(input())):
    n, m = list(map(int, input().split()))
    if m % 2 == 0:
        print((m // 2) * n)
    else:
        print((m // 2) * n + (n + 1) // 2)