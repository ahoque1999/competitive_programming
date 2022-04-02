# balance
def bal(s):
    a = sum([1 for si in s if si == 'a'])
    b = sum([1 for si in s if si == 'b'])
    if a == b and a != 0:
        return True
    return False

# first pair of indices
def ind(s):
    for beg in range(n):
        for leng in range(1, n - beg + 1):
            sub = s[beg: beg + leng]
            if bal(sub):
                return (beg + 1, beg + leng)
    return (-1, -1)

for _ in range(int(input())):
    n = int(input())
    s = input()

    indices = ind(s)
    print(f'{indices[0]} {indices[1]}')
