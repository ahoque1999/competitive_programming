digits = list(map(int, input().split()))

number_256 = min([digits[0], digits[2], digits[3]])
digits[0] -= number_256
number_32 = min([digits[0], digits[1]])

print(256 * number_256 + 32 * number_32)