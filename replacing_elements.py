for i in range(int(input())):
    n, d = list(map(int, input().split()))
    x = list(map(int, input().split()))
    
    largest = max(x)
    smallest = min(x)
    x.remove(smallest)
    smallest2 = min(x)

    if largest <= d:
        print("YES")
    elif (smallest + smallest2) <= d:
        print("YES")
    else:
        print("NO")