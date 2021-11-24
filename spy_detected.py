for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] == a[1]:
        non_unique = a[0]
    elif a[0] == a[2]:
        print(2)
        continue
    else:
        print(1)
        continue
    for i,ai in enumerate(a):
        if ai != non_unique:
            print(i + 1)