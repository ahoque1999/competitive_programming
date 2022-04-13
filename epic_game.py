def gcd(num_1, num_2):
    """ get greatest common divisor """

    while num_2:
        num_1, num_2 = num_2, num_1%num_2
    return num_1

numbers = list(map(int, input().split()))

count = 0
while numbers[2] >= gcd(numbers[2], numbers[count % 2]):
    # print(f"{numbers[2]} {numbers[count % 2]}")
    numbers[2] -= gcd(numbers[2], numbers[count % 2])
    count += 1

print(1 - count % 2)