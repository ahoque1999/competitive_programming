for i in range(int(input())):
    n = int(input())

    numbers = list(range(1, n + 1))
    for i in range(0, n - 1, 2):
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    if n % 2 == 1:
        numbers[-1], numbers[-2] = numbers[-2], numbers[-1] 
    
    for number in numbers:
        print(number, end=" ")
    print()