for iteration in range(int(input())):
    a, b, c = list(map(int, input().split()))

    maximum = max([a,b,c])

    if a > b and a > c:
        A = 0
    else:
        A = maximum + 1 - a
    if b > a and b > c:
        B = 0
    else:
        B = maximum + 1 - b
    if c > b and c > a:
        C = 0
    else:
        C = maximum + 1 - c

    print(f"{A} {B} {C}")