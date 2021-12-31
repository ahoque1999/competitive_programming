for iteration in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a = sorted(a)
    remainder = 0
    for i in range(n - 2 * k):
        remainder += a[0]
        del a[0]

    total = remainder
    for i in range(k):
        if a[i] < a[i + k]:
            total += 0
        else:
            total += 1
    print(total)