for iteration in range(int(input())):
    n = int(input())

    remainder_by_7 = n % 7
    
    if remainder_by_7 == 0:
        print(n)
        continue

    remainder_by_10 = n % 10

    if remainder_by_10 > remainder_by_7:
        print(n - remainder_by_7)
    else:
        print(n + 7 -remainder_by_7)