for i in range(int(input())):
    n = int(input())

    iterations = n // 2020 + 1

    found = False
    for i in range(iterations):
        if i * 2020 + (iterations - 1 - i) * 2021 == n:
            found = True
    
    print("YES") if found else print("NO")