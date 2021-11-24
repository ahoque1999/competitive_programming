n = int(input())
capacity = -1
current = 0
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    current = current - a + b
    if current > capacity:
        capacity = current
print(capacity) 