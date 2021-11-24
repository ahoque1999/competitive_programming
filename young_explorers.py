for i in range(int(input())):
    n = int(input())
    e = list(map(int, input().split()))

    sorted_e = sorted(e)

    groups = 0
    temp_size = 0
    for i in range(n):
        temp_size += 1
        if temp_size == sorted_e[i]:
            groups += 1
            temp_size = 0

    print(groups)