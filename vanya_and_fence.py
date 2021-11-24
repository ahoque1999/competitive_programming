[n, h] = map(int,input().split())
a = map(int,input().split())
width = 0
for ai in a:
    if ai > h:
        width += 2
    else:
        width += 1

print(width)