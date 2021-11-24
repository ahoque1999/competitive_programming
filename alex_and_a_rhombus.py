n = int(input())

cells = [0] * 100
cells[0] = 1
for i in range(2, 101):
    cells[i - 1] = cells[i - 2] + 4 * (i - 1) 

print(cells[n - 1])