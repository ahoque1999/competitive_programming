s = input()
number_unique = (len(''.join(set(s))))
if number_unique % 2 is 0:
    print("CHAT WITH HER!")
else: 
    print("IGNORE HIM!")