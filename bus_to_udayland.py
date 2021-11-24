dict_string_to_num = {
    "OO" : 1,
    "OX" : 2,
    "XO" : 3,
    "XX" : 4
}

dict_num_to_string = {
    0 : "++",
    1 : "OO",
    2 : "OX",
    3 : "XO",
    4 : "XX"
}

def check_for_1(list):
    for item in list:
        if item == 1:
            return True
    return False

def convert(list):
    for i in range(len(list)):
        if list[i] == 1:
            list[i] = 0
            break

def print_bus(list):
    n = len(list) // 2
    for i in range(n):
        print(f"{dict_num_to_string[converted_list[2 * i]]}|{dict_num_to_string[converted_list[2 * i + 1]]}")
         

converted_list = []
n = int(input())
for i in range(n):
    s = input()

    converted_list.append(dict_string_to_num[s[:2]])
    converted_list.append(dict_string_to_num[s[3:]])

if check_for_1(converted_list):
    convert(converted_list)
    print("YES")
    print_bus(converted_list)
else:
    print("NO")
    