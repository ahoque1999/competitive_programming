first_input = input()
second_input = input()

for i, char in enumerate(first_input):
    # print(char)
    if char != second_input[i]:
        print("1", end="")
    else:
        print("0", end="")