for i in range(int(input())):
    n, m, k = list(map(int, input().split()))

    sum_n = n - 1 
    sum_m = n * (m - 1)
    print("YES") if (sum_n + sum_m) == k else print("NO")