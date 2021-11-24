for iteration in range(int(input())):
    # ignore q since it is always 0 in this case
    n = list(map(int, input().split()))[0]

    a = list(map(int, input().split()))

    env = "local maximum"
    total = 0
    for index in range(n):
        if env == "local maximum":
            if index == n - 1:
               total += a[index]
               continue
            if a[index] > a[index + 1]:
                total += a[index]
                env = "local minimum"
                continue
        if env == "local minimum":
            if index == n - 1:
                continue
            if a[index] < a[index + 1]:
                total -= a[index]
                env = "local maximum"
                continue
    print(total)