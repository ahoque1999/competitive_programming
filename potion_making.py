def gcd(num_1, num_2):
    """ get greatest common divisor """

    while num_2:
        num_1, num_2 = num_2, num_1%num_2
    return num_1


for _ in range(int(input())):
    k = int(input())

    print(100 // gcd(k, 100))