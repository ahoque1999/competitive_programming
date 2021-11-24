for i in range(int(input())):
    n = int(input())

    powers_of_two = [1] * 31
    for i in range(1, 31):
        powers_of_two[i] = 2 * powers_of_two[i -1]

    for i in range(31):
        if n < powers_of_two[i]:
            print(powers_of_two[i - 1] - 1)
            break