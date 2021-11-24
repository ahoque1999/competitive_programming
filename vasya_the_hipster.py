a,b = list(map(int, input().split()))
print(a,(b - a) // 2) if b > a else print(b, (a - b) // 2)