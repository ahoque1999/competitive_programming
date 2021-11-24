for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    result = 1
    for i in range(n):
        if a[i] == 1 and i % 2 == 0:
            result = 0
        elif a[i] == 1 and i % 2 == 1:
            result = 1
        else:
            result = 1 - result
            break
    
    print("First") if result == 0 else print("Second")