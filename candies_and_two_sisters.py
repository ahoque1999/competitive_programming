n = int(input())
for i in range(n):
    number = int(input())
    print(number // 2) if number % 2 == 1 else print((number - 1) // 2)