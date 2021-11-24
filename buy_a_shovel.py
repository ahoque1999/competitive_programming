k,r = list(map(int, input().split()))
for i in range(1, 11):
    last_digit = (k * i) % 10
    if last_digit == r or last_digit == 0:
        print(i)
        break

