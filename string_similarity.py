for i in range(int(input())):
    n = int(input())
    s = input()
    
    print("".join([s[2 * i] for i in range(n)]))