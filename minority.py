for _ in range(int(input())):
    s = input()

    num_0 = sum([1 for si in s if si == '0'])
    num_1 = sum([1 for si in s if si == '1'])

    if num_0 == num_1:
        print(num_1 - 1)
    elif num_0 == 0 or num_1 == 0:
        print(0)
    else:
        print(min([num_0, num_1]))