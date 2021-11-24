def test_case():
    n = int(input())
    if n % 4 != 0:
        print("NO")
    else:
        print("YES")
        for i in range(n // 2):
            print(2 * i + 2, end=" ")
        for i in range(n // 2 - 1):
            print(2 * i + 1, end=" ")
        print(n + n // 2 - 1)

t = int(input())
for i in range(t):
    test_case()