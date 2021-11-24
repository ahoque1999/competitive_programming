n, d = list(map(int, input().split()))
s = input()

lilies = [i + 1 for i in range(n) if s[i] == "1"]
start = 1
count = 0
while True:
    count += 1
    jump = max([lily for lily in lilies if lily <= start + d])

    if jump == start:
        print(-1)
        break
    
    if jump == n:
        print(count)
        break

    start = jump