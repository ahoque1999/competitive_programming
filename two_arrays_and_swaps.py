def test_case():
    n, k = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))[::-1]
    for i in range(k):
        if a[i] >= b[i]:
            break
        else:
            a[i] = b[i]
    print(sum(a))


t = int(input())
for i in range(t):
    test_case()