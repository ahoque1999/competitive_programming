for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1 and a[0] % 2 == 1:
        print(-1)
    elif a[0] % 2 == 0:
        print(1)
        print(1)
    elif a[1] % 2 == 0:
        print(1)
        print(2)
    else:
        print(2)
        print("1 2")