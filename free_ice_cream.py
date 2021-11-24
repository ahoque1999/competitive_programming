n, x = list(map(int, input().split()))

count_distressed = 0
for i in range(n):
    record = input().split()
    # True indicates add, False subtract
    sign = True if record[0] == "+" else False
    di = int(record[1])

    if sign:
        x += di
    else:
        if di <= x:
            x -= di
        else:
            count_distressed +=1

print(x,count_distressed)