def check(list, n):
    for i in list:
        if i > end_value:
            return True
    return False

for i in range(int(input())):
    a, b, c, n = list(map(int, input().split()))
    end_value = sum([a, b, c, n]) // 3
    if sum([a, b, c, n]) % 3 != 0:
        print("NO")
    elif check([a, b, c], end_value):
        print("NO")
    else:
        print("YES")