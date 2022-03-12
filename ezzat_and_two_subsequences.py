for iteration in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    largest = max(a)
    a.remove(largest)

    print(largest + sum(a)/len(a))