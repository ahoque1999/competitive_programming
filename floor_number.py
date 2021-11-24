for i in range(int(input())):
    n, x = list(map(int, input().split()))
    if n <= 2:
        print(1)
    else:
        print(1 + (n - 2) // x) if (n - 2) % x == 0 else print(2 + (n - 2) //x) 