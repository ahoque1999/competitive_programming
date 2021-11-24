def results(n):
    start = 0
    numbers = []
    for i in range(n):
        start = i * 10 + n
        while True:
            if start >= 10 * n:
                break
            numbers.append(start)
            start += n
    return numbers

for i in range(int(input())):
    q, d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    numbers = results(d)
    threshold = d * 10 if d > 1 else 0
    for i in range(q):
        print("YES") if a[i] >= threshold or a[i] in numbers else print("NO")            