n = int(input())
s = input()
comparing_character = s[0]
final_list = [s[0]]
for i in range(1,n):
    if s[i] is not comparing_character:
        comparing_character = s[i]
        final_list.append(comparing_character)
print(len(s) - len(final_list))