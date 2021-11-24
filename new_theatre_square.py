for i in range(int(input())):
    n, m, x, y = list(map(int, input().split()))
    twos = 0
    ones = 0
    for i in range(n):
        s = input()
        range_iter = iter(range(m))
        for i in range_iter:
            if s[i] == ".":
                if i == m -1:
                    ones += 1
                elif s[i + 1] == ".":
                    twos += 1 
                    next(range_iter)
                else:
                    ones += 1
    print(min([y * twos + x * ones, x * 2 * twos + x * ones]))