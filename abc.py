for iteration in range(int(input())):
    n = int(input())
    s = input()

    if s == "11" or s == "00":
        print("NO")
        continue

    print("YES") if n <= 2 else print("NO")