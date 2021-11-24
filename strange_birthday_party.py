for iteration in range(int(input())):
    n, m = list(map(int, input().split()))
    k = list(map(int, input().split()))
    c = list(map(int, input().split()))

    temp = sorted([c[element - 1] for element in k])[::-1]

    for index in range(min([n, m])):
        if temp[index] > c[index]:
            temp[index] = c[index]
        else:
            break
    
    print(sum(temp))
