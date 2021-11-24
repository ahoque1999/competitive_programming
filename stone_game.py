def check_for_1(s):
    for char in s:
        if char == "1":
            return True
    return False

def recurse(s):
    if not check_for_1(s):
        return 0
    forward_dist = s.index("1")
    back_dist = s[::-1].index("1")
    return recurse(s[1:]) + 1 if forward_dist < back_dist else recurse(s[:-1]) + 1

def conv(i,a):
    return "1" if i == max(a) or i == min(a) else "0"

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a_conv = ""
    for i in a:
        a_conv = a_conv + conv(i,a)
    print(recurse(a_conv))