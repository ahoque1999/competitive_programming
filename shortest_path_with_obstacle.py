for i in range(int(input())):
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = list(map(int, input().split()))

    if a[0] != b[0] and a[1] != b[1]:
        print(abs(b[1] - a[1]) + abs(b[0] - a[0]))
    elif (f[0] == a[0] and ((a[1] < f[1] < b[1]) or (b[1] < f[1] < a[1]))) or (f[1] == a[1] and ((a[0] < f[0] < b[0]) or (b[0] < f[0] < a[0]))):
        print(abs(b[1] - a[1]) + abs(b[0] - a[0]) + 2)
    else:
        print(abs(b[1] - a[1]) + abs(b[0] - a[0]))