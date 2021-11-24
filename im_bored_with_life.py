a,b = list(map(int, input().split()))

number = min([a,b])
result = 1
for i in range(1, number + 1):
    result *= i

print(result)