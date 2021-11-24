def check_closed(string):
    l = 0
    r = 0
    for char in string:
        if char == "(":
            l += 1
        else:
            r += 1
    return True if l == r else False

def count_rbs_prefix(string):
    total = 0
    temp_total = 0
    for char in string:
        if char == "(":
            temp_total -= 1
        else:
            temp_total += 1
        if temp_total == 0:
            total += 1
    
    print(total)

total = 0
n = int(input())
for iteration in range(n):
    string = input()
    if check_closed(string):
        total += count_rbs_prefix(string)
    