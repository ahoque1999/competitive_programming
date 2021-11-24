MAX = 10800010
n = int(input())
sum = 0
k = 0
t = 10

for i in range(MAX):
    t = t + 9
    p = t
    while(p >= 1):
        sum = sum + p % 10
        p = p // 10
    if sum == 10:
        k += 1
        sum = 0
    else:
        sum = 0
    if k == n:
        print(t)
        break