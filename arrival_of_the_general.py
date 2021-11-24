n = int(input())
a = list(map(int, input().split()))
# find the first instance of max
maximum = a.index(max(a))
# print(maximum)
# find the last instance of min
minimum = n - 1 - a[::-1].index(min(a))
# print(minimum)
if maximum > minimum:
    print(maximum + n -1 - minimum - 1)
else:
    print(maximum + n - 1 -minimum)
