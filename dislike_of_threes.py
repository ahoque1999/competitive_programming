numbers = [0] * 1000
start = 1
number = start
for i in range(1000):
    while True:
        if number % 3 == 0 or number % 10 == 3:
            number += 1
        else:
            break
    numbers[i] = number
    number += 1

for iteration in range(int(input())):
    print(numbers[int(input()) - 1])