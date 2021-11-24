n = int(input())
a = list(map(int, input().split()))

cumulative_sum = [0] * n
cumulative_sum[0] = a[0]
for i in range(1, n):
    cumulative_sum[i] = cumulative_sum[i - 1] + a[i]

sorted_a = sorted(a)
sorted_cumulative_sum = [0] * n
sorted_cumulative_sum[0] = sorted_a[0]
for i in range(1, n):
    sorted_cumulative_sum[i] = sorted_cumulative_sum[i - 1] + sorted_a[i]

m = int(input())
for i in range(m):
    type_, l, r = list(map(int, input().split()))
    l -= 1
    r -= 1
    if type_ == 1:
        print(cumulative_sum[r]) if l == 0 else print(cumulative_sum[r] - cumulative_sum[l - 1])
    else:
        print(sorted_cumulative_sum[r]) if l == 0 else print(sorted_cumulative_sum[r] - sorted_cumulative_sum[l - 1])