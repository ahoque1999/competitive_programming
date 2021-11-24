for i in  range(int(input())):
    s = input()
    n = len(s)
    found = False

    counts = [0] * n
    counts[0] = 0 if s[0] == "1" else 1
    for i in range(1, n):
        if s[i] == "0" and s[i - 1] == "1":
            counts[i] = counts[i - 1] + 1
        elif s[i] == "0":
            counts[i] = counts[i - 1]
        else:
            counts[i] = counts[i - 1]
            
        if counts[i] == 2:
            found = True
            break
    print(counts[-1]) if found == False else print(2)
    