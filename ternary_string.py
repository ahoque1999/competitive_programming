for i in range(int(input())):
    a = list(map(int, list(input()))) 
    n = len(a)

    numbers = [a[0]]
    temp_number = a[0]
    start = [0]
    end = []

    for i in range(1, n):
        if a[i] != a[i - 1]:
            end.append(i - 1)
            start.append(i)
            temp_number = a[i]
            numbers.append(a[i])
    end.append(n - 1)

    lengths = []
    for i in range(len(numbers) - 2):
        if numbers[i] != numbers[i + 1] and numbers[i] != numbers[i + 2] and numbers[i + 1] != numbers[i + 2]:
            lengths.append(start[i + 2] - end[i] + 1)

    print(min(lengths)) if len(set(numbers)) == 3 else print(0)