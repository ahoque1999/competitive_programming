for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even = sum([1 for ai in a if ai % 2 == 0])
    odd = sum([1 for ai in a if ai % 2 == 1])
    if n % 2 == 0 and (even != n // 2 or odd != n//2):
        print(-1)
        continue
    elif n % 2 == 1 and (even != n //2 + 1 or odd != n // 2):
        print(-1)
        continue
    error = sum([1 for i, ai in enumerate(a) if i % 2 != ai % 2])
    print(error //2 )
