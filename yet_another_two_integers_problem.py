def task():
    a,b = list(map(int, input().split()))
    difference = str(b -a) if b > a else str(a -b)
    reverse_difference = difference[::-1]
    count = 0
    for i in range(len(reverse_difference)):
        if i == 0 and reverse_difference[i] != '0':
            count += 1
        else:
            count += int(int(reverse_difference[i]) * 10 ** (i - 1))
    print(count)

t = int(input())
for i in range(t):
    task()