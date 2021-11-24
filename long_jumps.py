for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a = a[::-1]
    results = [0] * n
    for i in range(n):
        if a[i] > i:
            results[i] = a[i]
        else:
            results[i] = a[i] + results[i - a[i]]
    
    print(max(results))