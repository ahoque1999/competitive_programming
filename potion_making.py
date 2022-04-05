def gcd(x, y):
    
    y = max([x, y])
    x = min([x, y])
    
    while y:
        x, y = y, x % y
    return x

for _ in range(int(input())):
    k = int(input())

    print(100 // gcd(k, 100))