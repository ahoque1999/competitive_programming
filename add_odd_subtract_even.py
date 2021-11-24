for i in range(int(input())):
    a, b = list(map(int, input().split()))
    if a < b:
        if (a + b) % 2 == 1:
            print(1)
        else: 
            print(2)
    elif a > b:
        if (a + b) % 2 == 1:
            print(2)
        else: 
            print(1)
    else:
        print(0)