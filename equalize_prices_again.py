for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)
    print(total // n) if total % n == 0 else print(total // n + 1) 