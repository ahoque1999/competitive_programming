for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    odd = [ai for ai in a if ai % 2 == 1]
    eve = [ai for ai in a if ai % 2 == 0]

    for ele in odd:
        print(ele, end=' ')
    
    for ele in eve:
        print(ele, end=' ')
    
    print()