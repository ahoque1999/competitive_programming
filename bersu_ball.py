n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = sorted(list(map(int, input().split())))

pairs = 0
checkpoint = 0
for i in range(n):
    boy = a[i]

    for i in range(checkpoint, m):
        if boy == b[i] or boy == b[i] - 1 or boy == b[i] + 1:
            pairs += 1
            checkpoint = i + 1
            break
        if boy > b[i]:
            checkpoint += 1    
print(pairs)