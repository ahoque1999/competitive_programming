for iteration in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    sum_a = sum(a)
    k = sum_a / n

    if k * 10 % 5 != 0:
        print(0)
        continue

    pairs = {}
    total = 0
    required = 2 * k

    for element in a:
        total += pairs.get(required - element, 0)
        if element in pairs.keys():
            pairs[element] += 1
        else:
            pairs[element] = 1

    print(total)