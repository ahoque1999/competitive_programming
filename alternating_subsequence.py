for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # direction = True if positive block, False if negative
    if a[0] > 0:
        direction = True
    else:
        direction = False

    temp = a[0]
    total = 0
    for i in range(1, n):
        if direction and a[i] > 0 and a[i] > temp:
            temp = a[i]
        
        if direction and a[i] < 0:
            total += temp
            direction = False
            temp = a[i]
        
        if not direction and a[i] < 0 and a[i] > temp:
            temp = a[i]
        
        if not direction and a[i] > 0:
            total += temp
            direction = True
            temp = a[i]
    total += temp
    print(total)    