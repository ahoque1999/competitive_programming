for iteration in range(int(input())):
    a, b, c = list(map(int, input().split()))

    smaller = min([a,b])
    larger = max([a,b])

    if larger < 2 * smaller:
        print(-1)
        continue
    
    half = larger - smaller
    n = half * 2

    if c > n:
        print(-1)
        continue

    if c <= half:
        print(c + half)
    else:
        print(c - half)