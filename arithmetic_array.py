for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)
    if total == n:
        print(0)
    elif total < n:
        print(1)
    else:
        print(total - n)