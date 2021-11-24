n = int(input())
x = list(map(int, input().split()))

s =[]
d =[]
for i in range(n):
    index = 0 if x[0] > x[-1] else -1
    if i % 2 == 0:
        s.append(x.pop(index))
    else:
        d.append(x.pop(index))
        
print(f'{sum(s)} {sum(d)}')