n = int(input())

# if odd follow 2 n^2 + 2 n where n is nth odd number
if n % 2 == 1:
    n = (n + 1) //2
    print(2 * n **2 + 2 * n)
else:
    n = n // 2
    print(n ** 2 + 2 * n + 1)