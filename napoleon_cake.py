for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]

    layers = [0] * n
    for i in range(n):
        current = a[i]
        if current != 0:
            numbers = [max([0, a[j] - (current - (j - i)) ]) for j in range(i, min(i + current, n))]
            next_index = min(i + current, n - 1)
            numbers.append(a[next_index])
            a[next_index] = max(numbers)
            for j in range(i, min(i + current, n)):
                a[j] = 0
                layers[j] = 1
    layers = layers[::-1]

    for layer in layers:
        print(layer, end=" ")
    print()