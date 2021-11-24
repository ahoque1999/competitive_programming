for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    num_odd = sum([1 for ai in a if ai % 2 == 1])
    num_even = sum([1 for ai in a if ai % 2 == 0])

    if 1 <= num_odd < n:
        print("YES")
    elif num_odd == n and n % 2 == 1:
        print("YES")
    else:
        print("NO)