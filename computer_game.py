for iteration in range(int(input())):
    n = int(input())
    r1 = input()
    r2 = input()

    found = False
    for index in range(n):
        if r1[index] == "1" and r2[index] == "1":
            found = True
            break
    
    print("NO") if found else print("YES")