def gcd(list):
    big = max(list)
    small = min(list)
    if small == 0:
        return big
    return small if big % small == 0 else gcd([small, big % small])

numbers = list(map(int, input().split()))

count = 0
while numbers[2] >= gcd([numbers[2], numbers[count % 2]]):
    # print(f"{numbers[2]} {numbers[count % 2]}")
    numbers[2] -= gcd([numbers[2], numbers[count % 2]])
    count += 1

print(1 - count % 2)