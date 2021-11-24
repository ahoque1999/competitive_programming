for i in range(int(input())):
    s = list(map(int, input().split()))

    first = max(s)
    s_new = [si for si in s if si != first]
    second = max(s_new)
    # left = True, right = False
    first_position = True if s.index(first) == 0 or s.index(first) == 1 else False
    second_postion = True if s.index(second) == 0 or s.index(second) == 1 else False

    print("NO") if (first_position and second_postion) or (not first_position and not second_postion) else print("YES")