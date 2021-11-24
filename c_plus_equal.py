for i in range(int(input())):
    a, b, n = list(map(int, input().split()))
    numbers = sorted([a,b])
    while numbers[-1] <= n:
        numbers.append(numbers[-1] + numbers[-2])
    print(len(numbers) - 2)