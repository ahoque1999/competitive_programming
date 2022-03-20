def check(indices):
    for index in indices:
        if index % 2 == 0:
            return True
    return False

    
for iteration in range(int(input())):
    s = input()
    c = input()

    n = len(s)

    indices = [i for i in range(n) if s[i] == c]

    print("YES") if check(indices) else print("NO")