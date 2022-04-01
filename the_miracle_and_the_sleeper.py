for _ in range(int(input())):
    l, r = list(map(int, input().split()))

    bes = r // 2 + 1
    if l <= bes:
        print(r % bes)
    else:
        print(r % l)