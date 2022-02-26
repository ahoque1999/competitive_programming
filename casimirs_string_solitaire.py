for iteration in range(int(input())):
    string = input()
    num_A = sum([1 for char in string if char == "A"])
    num_B = sum([1 for char in string if char == "B"])
    num_C = sum([1 for char in string if char == "C"])

    print("YES") if num_A + num_C == num_B else print("NO")