for iteration in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    maxi = -1
    for i in range(1, n):
        if a[i - 1] * a[i] > maxi:
            maxi = a[i -1] * a[i]
    
    print(maxi)