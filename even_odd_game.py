for i in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))[::-1]

    alice = 0
    bob =0
    even = True
    for i in range(n):
        if even:
            if a[i] % 2 == 0:
                alice += a[i]
            even = False
        else:
            if a[i] % 2 == 1:
                bob += a[i]
            even = True
    
    if alice == bob:
        print("Tie")
    elif alice > bob:
        print("Alice")
    else:
        print("Bob")