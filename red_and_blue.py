for i in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    consecutive_sum_n = [0] * n
    consecutive_sum_n[0] = r[0]
    for i in range(1, n):
        consecutive_sum_n[i] = consecutive_sum_n[i - 1] + r[i]
    consecutive_sum_n.append(0)

    consecutive_sum_m = [0] * m
    consecutive_sum_m[0] = b[0]
    for i in range(1, m):
        consecutive_sum_m[i] = consecutive_sum_m[i - 1] + b[i]
    consecutive_sum_m.append(0)

    print(max(consecutive_sum_m) + max(consecutive_sum_n))