for i in range(int(input())):
    c, r = list(map(int, input().split()))
    if c == 1 or r == 1:
        print("YES")
    elif c == 2 and r == 2:
        print("YES")
    else:
        print("NO")