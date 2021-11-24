for i in range(int(input())):
    s = input()
    
    n = len(s)

    left_check_11 = False
    right_check_00 = False

    for i in range(1, n):
        if s[i] == "1" and s[i - 1] == "1":
            left_check_11 = True
        if s[i] == "0" and s[i - 1] == "0" and left_check_11:
            right_check_00 = True

    print("NO") if right_check_00 else print("YES")