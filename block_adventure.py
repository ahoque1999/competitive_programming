for iteration in range(int(input())):
    n, m, k = list(map(int, input().split()))
    h = list(map(int, input().split()))

    possible = True
    store = m
    for index in range(n - 1):
        lowest_possible = max([0, h[index + 1] - k])
        if h[index] < lowest_possible:
            if h[index] + store < lowest_possible:
                possible = False
                break
            else:
                store -= lowest_possible - h[index]
        else:
            store += h[index] - lowest_possible
    print("YES") if possible else print("NO")