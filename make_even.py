for iteration in range(int(input())):
    n = int(input())

    last_digit = n % 10

    if last_digit % 2 == 0:
        print(0)
        continue

    first_digit = int(str(n)[0])

    if first_digit % 2 == 0:
        print(1)
        continue

    even_digit_present = False

    digits = list(str(n))
    digits = list(map(int, digits))
    for digit in digits:
        if digit % 2 == 0:
            even_digit_present = True
            break
    
    print(2) if even_digit_present else print(-1)