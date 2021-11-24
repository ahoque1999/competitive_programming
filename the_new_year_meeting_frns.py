x = list(map(int, input().split()))
x.sort()
# best meeting point is the median as it results in the shortest total distance in 1D
# print sum
print(x[1] - x[0] + x[2] - x[1])