for iteration in range(int(input())):
    list_of_numbers = list(map(int, input().split()))
    print(f"{list_of_numbers[0]} {list_of_numbers[1]} {list_of_numbers[-1] - list_of_numbers[0] - list_of_numbers[1]}")