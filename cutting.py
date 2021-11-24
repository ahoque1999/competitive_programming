n, B = list(map(int, input().split()))
a = list(map(int, input().split()))

odd_length = 0 
even_length = 0
indices = []
for index in range(n):
    if a[index] % 2 == 1:
        odd_length += 1
    else:
        even_length += 1
    if odd_length == even_length:
        indices.append(index)
        odd_length = 0
        even_length = 0

last_element = indices.pop(-1)

costs = sorted([abs(a[index + 1] - a[index]) for index in indices])

length = len(costs)
for index in range(length):
    B = B - costs[index]
    if B < 0:
        print(index)
        break

if sum(costs) <= B:
    print(length)
elif B >= 0:
    print(length)