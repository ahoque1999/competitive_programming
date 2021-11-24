s = input()
number_capital = sum(1 for i in s if i.isupper())
if number_capital > (len(s) - number_capital):
    print(s.upper())
else:
    print(s.lower())