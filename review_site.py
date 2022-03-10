for iteration in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))

    print(sum([1 for number in numbers if number == 1 or number == 3]))