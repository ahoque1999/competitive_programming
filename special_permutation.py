for i in range(int(input())):
    n = int(input())

    p = list(range(1, n + 1))
    p.reverse()
    if n % 2 ==1:
        p[0], p[n // 2] = p[n // 2], p[0]

    for pi in p:
        print(pi, end=" ")
    print()