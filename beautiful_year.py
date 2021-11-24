def check_if_beautiful_year(string):
    string = string.lower()
    list_string = list(string)
    list_string.sort()
    unique_list = list(set(string))
    unique_list.sort()
    if list_string == unique_list:
        return True
    else: 
        return False

y = int(input())
y += 1
string = str(y)
while not check_if_beautiful_year(string):
    y +=1
    string = str(y)
print(y)
