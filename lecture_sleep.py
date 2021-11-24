n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
t = list(map(int, input().split()))

flipped_t = [1 - number for number in t]

original_total = sum(a[index] * t[index] for index in range(n))
sums = [sum(a[index] * flipped_t[index] for index in range(k))]

for index in range(1, n - k + 1):
    current_change = sums[index - 1] - a[index - 1] * flipped_t[index - 1] + a[index + k - 1] * flipped_t[index + k - 1]
    sums.append(current_change)

print(original_total + max(sums))