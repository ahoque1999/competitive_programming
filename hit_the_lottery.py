n = int(input())
count = 0
denominations = [100, 20, 10, 5, 1]
for i in denominations:
    count += n // i
    n -= n//i *i
print(count)
