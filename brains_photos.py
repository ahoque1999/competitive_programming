def check_presence():
    colours = ['C', 'M', 'Y']
    check = False
    n, m = list(map(int, input().split()))
    for i in range(n):
        row = input().split()
        for colour in row:
            if colour in colours:
                check = True
    return check

print("#Color") if check_presence() else print("#Black&White")