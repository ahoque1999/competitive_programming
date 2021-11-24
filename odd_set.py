for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even = sum([1 for ai in a if ai % 2 == 0])
    odd = sum([1 for ai in a if ai % 2 == 1])
    print("Yes") if even == odd else print("No")