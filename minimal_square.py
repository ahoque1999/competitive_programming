for i in range(int(input())):
    numbers = sorted(list(map(int, input().split())))
    b, a = numbers
    if a > 2 * b:
        print(a * a)
    else:
        print(4 * b * b)