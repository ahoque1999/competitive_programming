for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a_unique = list(set(a))
    counts = [1] * len(a_unique)
    for i, a_unique_i in enumerate(a_unique):
        counts[i] = sum([1 for ai in a if ai == a_unique_i])
    print(max(counts))