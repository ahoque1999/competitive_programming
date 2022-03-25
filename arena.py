for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    min_ = min(a)

    print(sum([1 for ai in a if ai > min_]))