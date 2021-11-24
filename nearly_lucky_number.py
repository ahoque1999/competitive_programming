def check_lucky_number(string):
    for char in string:
        if char is not '4' and char is not '7':
            return False
    return True
    
s = input()
count = sum([1 for i in s if (i is '4' or i is '7')])

if check_lucky_number(str(count)):
    print("YES")
else:
    print("NO")
