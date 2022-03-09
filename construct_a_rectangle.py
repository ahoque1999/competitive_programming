def condition_2(sticks):
    if sticks[0] == sticks[1] and sticks[2] % 2 == 0:
        return True
    if sticks[0] == sticks[2] and sticks[1] % 2 == 0:
        return True
    if sticks[2] == sticks[1] and sticks[0] % 2 == 0:
        return True
    return False

for iteration in range(int(input())):
    sticks = list(map(int, input().split()))

    largest = max(sticks)
    if largest * 2 == sum(sticks):
        print("YES")
        continue

    print("YES") if condition_2(sticks) else print("NO")   