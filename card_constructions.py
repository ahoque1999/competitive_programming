def find_largest_smaller_than_number(list, number):
    start_index = 0
    final_index = len(list) - 1
    mid_index = start_index + (final_index - start_index) // 2

    while True:
        if number == list[mid_index]:
            return 0
        elif number < list[mid_index]:
            final_index = mid_index
            mid_index = start_index + (final_index - start_index) // 2
        elif number > list[mid_index]:
            start_index = mid_index
            mid_index = start_index + (final_index - start_index) // 2
        
        if start_index == mid_index:
            return number - list[mid_index]

HEIGHT = 30000
counts = [0] * (HEIGHT + 1)
counts[1] = 2

for i in range(2, HEIGHT + 1):
    counts[i] = counts[i - 1] + (i) * 2 + i - 1

for i in range(int(input())):
    number = int(input())
    counter = 0
    while number != 0 and number != 1:
        remaining = find_largest_smaller_than_number(counts, number)
        counter += 1
        number = remaining
    print(counter)