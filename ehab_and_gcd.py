for i in range(int(input())):
    n = int(input())
    print(f"{n // 2} {n // 2}") if n % 2 == 0 else print(f"{1} {n - 1}")