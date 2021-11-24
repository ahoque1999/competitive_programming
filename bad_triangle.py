for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    sum = a[0] + a[1]
    print(f"1 2 {n}") if sum <= a[-1] else print(-1)