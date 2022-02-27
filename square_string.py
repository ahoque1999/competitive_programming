for iteration in range(int(input())):
    string = input()
    n = len(string)
    if n % 2 == 1:
        print("NO")
    else:
        if string[:n//2] == string[n//2:]:
            print("YES")
        else:
            print("NO")