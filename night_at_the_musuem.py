import string

dict ={}
for i, letter in enumerate(list(string.ascii_lowercase)):
    dict[letter] = i

s = input()

start = "unassigned"

def find_min_length(char):
    global start
    if start == "unassigned":
        start = "a"
    end = char
    number = min([abs(dict[end] - dict[start]), abs(dict[end] + 26 - dict[start]), abs(dict[end] - dict[start] - 26)])
    start = char
    return number 

print(sum([find_min_length(char) for char in s]))