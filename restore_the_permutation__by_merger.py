for i in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    unique = []
    for pi in p:
        if pi not in unique:
            unique.append(pi)
            print(pi, end=" ")
    print()