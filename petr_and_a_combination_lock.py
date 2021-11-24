n = int(input())

degrees = []
for iteration in range(n):
    degrees.append(int(input()))

found = False
iterations = 2 ** n
# creat all 2^n possiblities
for iteration in range(iterations):
    binary_list = [0] * n

    count = n
    while True:
        binary_list[count - 1] = iteration % 2
        iteration = iteration // 2

        if iteration == 0:
            break

        count -= 1
    
    for index in range(n):
        if binary_list[index] == 0:
            binary_list[index] = -1

    # check if specific sequence of -1 and 1 add up to a multiple of 360 including 0
    summation = sum([binary_list[iteration] * degrees[iteration] for iteration in range(n)])

    if summation % 360 == 0:
        found = True
        break

print("YES") if found else print("NO")