for iteration in range(int(input())):
    n = int(input())
    rows = []
    for row in range(n):
        rows.append(input())
    
    # iterate through all the elements
    error = False
    for row in range(n):
        for column in range(n):
            if row == n - 1:
                continue
            if column == n - 1:
                continue

            if rows[row][column] == "1":
                if rows[row + 1][column] == "1" or rows[row][column + 1] == "1":
                    continue
                else:
                    error = True
                    break
        if error == True:
            break
    
    print("NO") if error else print("YES")