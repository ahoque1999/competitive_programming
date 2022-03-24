import math

for _ in range(int(input())):
    k = int(input())

    q = k ** (1 / 2)
    q = math.floor(q)
    r = k - q ** 2

    if r == 0:
        print(f"{q} 1")
    elif r <= q + 1:
        print(f"{r} {q + 1}")
    else:
        print(f"{q + 1} {q + 1 - (r - q - 1)}")