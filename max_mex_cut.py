for i in range(int(input())):
    n = int(input())
    s1 = list(map(int, list(input())))
    s2 = list(map(int, list(input())))
    numbers = [s1[i] + s2[i] for i in range(n)]

    total = 0

    range_iter = iter(range(n))
    for i in range_iter:
        if i == n - 1:
            if numbers[i] == 1:
                total += 2
            elif numbers[i] == 0:
                total += 1
            break

        if numbers[i] == 1:
            total += 2
        elif numbers[i] == 0 and numbers[i + 1] == 2:
            total += 2
            next(range_iter, None)
        elif numbers[i] == 2 and numbers[i + 1] == 0:
            total += 2
            next(range_iter, None)
        elif numbers[i] == 0:
            total += 1        

    print(total)