for i in range(int(input())):
    n = int(input())
    a = (list(map(int, input().split())))

    counts = [0] * n
    for ai in a:
        counts[ai - 1] += 1

    found = False
    for i in range(n):
        if counts[i] == 1:
            print(a.index(i + 1) + 1)
            found = True
            break

    if found == False:
        print(-1)