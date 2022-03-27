for _ in range(int(input())):
    field = []
    n = int(input())
    for __ in range(n):
        field.append(input())

    coor = []
    for i in range(n):
        for j in range(n):
            if field[i][j] == '*':
                coor.append((i, j))

    first_x = coor[0][0]
    first_y = coor[0][1]
    sec_x = coor[1][0]
    sec_y = coor[1][1]

    if first_x == sec_x and first_x == n - 1:
        coor.append((first_x - 1, first_y))
        coor.append((sec_x - 1, sec_y))
    elif first_x == sec_x:
        coor.append((first_x + 1, first_y))
        coor.append((sec_x + 1, sec_y))
    elif first_y == sec_y and first_y == n - 1:
        coor.append((first_x, first_y - 1))
        coor.append((sec_x, sec_y - 1))
    elif first_y == sec_y:
        coor.append((first_x, first_y + 1))
        coor.append((sec_x, sec_y + 1))
    else:
        coor.append((first_x, sec_y))
        coor.append((sec_x, first_y))

    for i in range(n):
        for j in range(n):
            temp = (i, j)
            if temp in coor:
                print('*', end='')
            else:
                print('.', end='')
        print()