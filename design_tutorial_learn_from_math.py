n = int(input())
if n % 4 == 0:
    print(n//2, n//2)
elif n % 2 == 0:
    print(n//2 + 1, n//2 - 1)
else:
    print(9, n - 9)