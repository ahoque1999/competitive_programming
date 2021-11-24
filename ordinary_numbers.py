for i in range(int(input())):
    n_string = input()
    n = int(n_string)
    digits = len(n_string)
    divisor = int("1" * digits)
    print((digits - 1) * 9 + n // divisor)