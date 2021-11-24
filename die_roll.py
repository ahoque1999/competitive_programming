x = list(map(int, input().split()))

def gcm(x):
    larger = max(x)
    smaller = min(x)
    return smaller if larger % smaller == 0 else gcm([larger, larger % smaller])

max_num = max(x)
numerator = 6 - max_num + 1
gcm = gcm([numerator, 6])
print(f"{numerator // gcm}/{6 // gcm}")