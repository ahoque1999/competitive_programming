n = int(input())
width = [0] * n
height = [0] * n
for i in range(n):
    width[i], height[i] = list(map(int, input().split()))

total = sum(width)
max_height = max(height)
max_height_index = height.index(max_height)
height_no_max = [height[i] for i in range(n) if i != max_height_index]
second_height = max(height_no_max)

for i in range(n):
    print((total - width[i]) * max_height, end = " ") if i != max_height_index else print((total - width[i]) * second_height, end = " ")
print()