for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)
    average = (total // n)
    print(sum([1 for ai in a if ai > average])) if total % n == 0 else print(-1)