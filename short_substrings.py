def test_case():
    b = input()
    for i in range(len(b) - 1):
        if i % 2 == 0:
            print(b[i], end="")
    print(b[-1])

t = int(input())
for i in range(t):
    test_case()