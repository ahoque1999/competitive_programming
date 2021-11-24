numbers = list(map(int, input().split()))
maximums = [1] * len(numbers)
for i in range(1, len(numbers)):
    comparisons = [1]
    for j in range(i):
        if numbers[i] > numbers[j]:
            comparisons.append(maximums[j] + 1)
    maximums[i] = max(comparisons)
print(max(maximums))
