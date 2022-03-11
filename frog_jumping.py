for iteration in range(int(input())):
    a, b, k = list(map(int, input().split()))
    quotient = k // 2
    remainder = k % 2

    print((a - b) * quotient + a * remainder)