def factorial(n):
    temp = 1
    for iteration in range(n):
        temp = temp * (iteration + 1)
    return temp

s1 = input()
s2 = input()

# get encoded s1
encode_s1 = [sum([1 for character in s1 if character == "+"]), sum([1 for character in s1 if character == "-"])]

# get encoded s2
encode_s2 = [sum([1 for character in s2 if character == "+"]), sum([1 for character in s2 if character == "-"])]

# check differences
plus_dif = encode_s1[0] - encode_s2[0]
minus_dif = encode_s1[1] - encode_s2[1]

if plus_dif == 0 and minus_dif == 0:
    print(1)
elif plus_dif < 0 or minus_dif < 0:
    print(0)
else:
    total = plus_dif + minus_dif
    print(factorial(total) / factorial(plus_dif) / factorial(minus_dif) / (2 ** total))