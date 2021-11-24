for i in range(int(input())):
    n = int(input())

    if n <= 30:
        print("NO")
    elif n == 36:
        print("YES")
        print("6 14 15 1")
    elif n == 44:
        print("YES")
        print("6 10 13 15")
    elif n == 40:
        print("YES")
        print("6 10 15 9")
    else:
        print("YES")
        print(f"6 10 14 {n - 30}")