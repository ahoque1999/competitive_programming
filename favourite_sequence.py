for i in range(int(input())):
    n = int(input())
    b = input().split()
    if n % 2 == 0:
        odd_list = b[: n // 2]
        even_list = b[n // 2 :][::-1]
    else:
        odd_list = b[: n // 2 + 1]
        even_list = b[n // 2 + 1 :][::-1]
    for i in range(n):
        if i % 2 == 0:
            print(odd_list[i // 2], end=" ")
        else:
            print(even_list[(i - 1) // 2], end=" ")
    print()
