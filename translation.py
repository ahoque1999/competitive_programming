s = input()
t = input()

s_list = []
for char in s:
    s_list.append(char)

t_list = []
for char in t:
    t_list.append(char)

s_list.reverse()

if  s_list == t_list:
    print("YES")
else:
    print("NO")



