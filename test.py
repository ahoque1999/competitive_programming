while True:
    a = input()
    if a == "end":
        break
    a = int(a)
    if a % 30 == 0:
        print(f"box {a // 30}")
    else:
        print(f"box {a // 30 + 1}")
        b = a % 30
        if b % 6 == 0:
            print(f"row {b // 6}")
        else:
            print(f"row {b // 6 + 1}")
            c = b % 6
            print(f"column {c}")
    