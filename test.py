# numbers = [0, 1, 2, 3]

# length = len(numbers)

# list_minus_two = [(element - 2 if element - 2 > -1 else None) for element in numbers]
# list_minus_one = [(element - 1 if element - 1 > -1 else None) for element in numbers]
# list_plus_one = [(element + 1 if element + 1 < length else None) for element in numbers]
# list_plus_two = [(element + 2 if element + 2 < length else None) for element in numbers]

# for i in range(length):
#     checks = [list_plus_two[i], list_minus_one[i], list_plus_one[i], list_plus_two[i]]
#     for check in checks:
#         if check is not None:
#             print(f"{numbers[i]} to {check}")

numbers = list(range(4))
length = len(numbers)
checks = [[] for i in range(length)]
for number in numbers:
    if number > 1:
        checks[number].append(number - 2)
    if number > 0:
        checks[number].append(number - 1)
    if number < length - 1:
        checks[number].append(number + 1)
    if number < length - 2:
        checks[number].append(number + 2)

print(checks)