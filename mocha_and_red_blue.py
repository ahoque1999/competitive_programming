for i in range(int(input())):
    n = int(input())
    s = list(input())

    first = [0] * n
    if s[0] == "?" and n == 1:
        print("R")
        continue
    elif s[0] == "?":
        first[0] = 1
        for i in range(1, n):
            if s[i] == "?":
                first[i] = first[i - 1] + 1
            else:
                break
        length = max(first)
        if length == n:
            length = length - 1
            s[length] = "B"
        if length % 2 == 1:
            s[0] = "R" if s[length] == "B" else "B"
        else:
            s[0] = "B" if s[length] == "B" else "R"
    for i in range(1, n):
        if s[i] == "?":
            s[i] = "R" if s[i - 1] == "B" else "B"

    for i in range(n):
        print(s[i], end="")
    print()