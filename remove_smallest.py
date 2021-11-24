def check_gap(list_of_numbers):
    for i in range(len(list_of_numbers) - 1):
        if (list_of_numbers[i + 1] - list_of_numbers[i]) > 1:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print("YES") if check_gap(numbers) else print("NO")