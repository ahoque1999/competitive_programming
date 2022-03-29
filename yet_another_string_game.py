for _ in range(int(input())):
    s = list(input())
    n = len(s)

    # a turns
    for i in range(0, n, 2):
        if s[i] == 'a':
            s[i] = 'b'
        else:
            s[i] = 'a'

    # b turns
    for i in range(1, n, 2):
        if s[i] == 'z':
            s[i] = 'y'
        else:
            s[i] = 'z'

    for char in s:
        print(char, end='')
    print()