n, k = list(map(int, input().split()))
y = list(map(int, input().split()))

count = sum([1 for yi in y if yi <= 5 - k])
print(count // 3)