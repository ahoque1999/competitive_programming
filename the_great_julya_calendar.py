def return_digits(n):
    digits = []
    while True:
        if n == 0:
            break
        digits.append(n % 10)
        n = n // 10
    return digits


n = int(input())
count = 0
while True:
    if n == 0:
        break

    n = n - max(return_digits(n))
    count = count + 1

print(count)
