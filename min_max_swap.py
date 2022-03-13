for iteration in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    minl = []
    maxl = []

    for index in range(n):
        minl.append(min(a[index],b[index]))
        maxl.append(max(a[index],b[index]))
    
    print(max(maxl) * max(minl))
