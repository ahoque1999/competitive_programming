for iteration in range(int(input())):
    a = int(input())
    numbers = list(map(int, input().split()))
    print(max(numbers) - min(numbers))