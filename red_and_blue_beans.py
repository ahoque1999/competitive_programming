for i in range(int(input())):
    r, b, d = list(map(int, input().split()))

    print("YES") if abs((r - b) / min([r, b])) <= d else print("NO")