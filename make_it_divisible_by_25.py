for iteration in range(int(input())):
    five_found = False
    zero_found = False
    number_reversed = input()[::-1]
    length = len(number_reversed)
    for index in range(length):
        if zero_found and (number_reversed[index] == "0" or number_reversed[index] == "5"):
            print(index - 1)
            break
        if number_reversed[index] == "0":
            zero_found = True
        
        if five_found and (number_reversed[index] == "2" or number_reversed[index] == "7"):
            print(index - 1)
            break
        if number_reversed[index] == "5":
            five_found = True