n = int(input())
s = input()

number_of_Ls = sum([1 for char in s if char == "L"])
number_of_Rs = sum([1 for char in s if char == "R"])

print(number_of_Ls + number_of_Rs + 1)