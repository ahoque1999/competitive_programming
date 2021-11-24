for i in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    smallest = a[0]
    print(sum([1 for ai in a if ai > smallest]))