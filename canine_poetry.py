characters = list("abcdefghijklmnopqrstuvwxyz")

def return_unique_integer(numbers):
    original = list(range(26))
    for element in numbers:
        if element in original:
            original.remove(element)
    return original[0]

for iteration in range(int(input())):

    poetry = list(input())
    length = len(poetry)
    checks = [[] for i in range(length)]
    for number in range(length):
        if number > 1:
            checks[number].append(number - 2)
        if number > 0:
            checks[number].append(number - 1)
        if number < length - 1:
            checks[number].append(number + 1)
        if number < length - 2:
            checks[number].append(number + 2)
    total = 0
    for i in range(length - 1):
        if i == length - 2:
            if poetry[i] == poetry[i + 1]:
                poetry[i + 1] = characters[return_unique_integer([characters.index(poetry[check]) for check in checks[i + 1]])]
                total += 1
            continue
        if poetry[i] == poetry[i + 1]:
            poetry[i + 1] = characters[return_unique_integer([characters.index(poetry[check]) for check in checks[i + 1]])]
            total += 1
        if poetry[i] == poetry[i + 2]:
            poetry[i + 2] = characters[return_unique_integer([characters.index(poetry[check]) for check in checks[i + 2]])]
            total += 1
    print(total)
