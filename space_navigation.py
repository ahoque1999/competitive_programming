for i in range(int(input())):
    px, py = list(map(int, input().split()))
    s = input()

    num_u = sum([1 for char in s if char == "U"])
    num_d = sum([1 for char in s if char == "D"])
    num_l = sum([1 for char in s if char == "L"])
    num_r = sum([1 for char in s if char == "R"])

    if px >= 0 and py >= 0:
        print("YES") if num_r >= px and num_u >= py else print("NO")
    elif px <= 0 and py >= 0:
        print("YES") if num_l >= -px and num_u >= py else print("NO")
    elif px <= 0 and py <= 0:
        print("YES") if num_l >= -px and num_d >= -py else print("NO")
    else:
        print("YES") if num_r >= px and num_d >= -py else print("NO")