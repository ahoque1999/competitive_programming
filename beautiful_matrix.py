def get_indices():
    global row_index
    global column_index
    s = input()
    if '1' in s.split():
        row_index = i 
        column_index = s.split().index('1')

for i in range(5):
    get_indices()

print(abs(row_index - 2) + abs(column_index - 2))