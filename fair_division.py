for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) % 2 == 1:
        print("NO")
    elif sum(a) // n == 2 and n % 2 == 1:
        print("NO")
    else:
        print("YES")

