n = int(input())
magnet = input()
count = 1
for i in range(n - 1):
    new_token = input()
    if new_token != magnet:
        count += 1
        magnet = new_token
print(count)
    