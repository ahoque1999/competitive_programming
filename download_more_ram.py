for iteration in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    lis = []
    for i in range(n):
        lis.append((a[i], b[i]))
    
    lis = sorted(lis)
    
    for i in range(n):
        if k >= lis[i][0]:
            k += lis[i][1]
        else:
            break

    print(k)