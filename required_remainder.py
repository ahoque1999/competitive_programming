for t in range(int(input())):
    x, y, n = list(map(int, input().split()))
    if n % x == y:
        print(n)
    elif n % x > y:
        print(n - n % x + y)
    elif n % x < y and n - n % x - x + y > 0:
        print(n - n % x - x + y)
    else:
        print(0)