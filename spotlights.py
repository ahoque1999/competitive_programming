n, m = list(map(int, input().split()))

array = []
for row_number in range(n):
    row = list(map(int, input().split()))
    array.append(row)

# build 1
array_1 = []
for row in array:
    new_row = [element for element in row]
    for column in range(1, m):
        if new_row[column - 1] == 1:
            new_row[column] = 1
    array_1.append(new_row)

# build 2
array_2 = []
for row in array:
    new_row = row[::-1]
    for column in range(1, m):
        if new_row[column - 1] == 1:
            new_row[column] = 1
    array_2.append(new_row[::-1])

# build 3
temp_array_3 = []
for column in range(m):
    new_row = [array[index][column] for index in range(n)]
    for element in range(1, n):
        if new_row[element - 1] == 1:
            new_row[element] = 1
    temp_array_3.append(new_row)
array_3 = []
for row in range(n):
    new_row = [temp_array_3[index][row] for index in range(m)]
    array_3.append(new_row)

# build 4
temp_array_4 = []
for column in range(m):
    new_row = [array[index][column] for index in range(n)][::-1]
    for element in range(1, n):
        if new_row[element - 1] == 1:
            new_row[element] = 1
    temp_array_4.append(new_row[::-1])
array_4 = []
for row in range(n):
    new_row = [temp_array_4[index][row] for index in range(m)]
    array_4.append(new_row)

total = 0
for row in range(n):
    for column in range(m):
        summation = array_1[row][column] + array_2[row][column] + array_3[row][column] + array_4[row][column] 
        total += summation if array[row][column] != 1 else 0

print(total)