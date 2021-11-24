n = int(input())
total_weight = 0
for triangle_number in range(n - 2):
    total_weight += 1 * (triangle_number + 2) * (triangle_number + 3)
print(total_weight)