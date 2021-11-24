for iteration in range(int(input())):
    n = int(input())
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))

    if n == 1:
        print(0)
        continue
    if n == 2:
        print(min(r1[-1], r2[0]))
        continue
    
    reversed_r1 = r1[::-1]
    cumulative_r1 = [0] * n
    for i in range(1, n):
        cumulative_r1[i] = cumulative_r1[i - 1] + reversed_r1[i - 1]
    cumulative_r1 = cumulative_r1[::-1]

    cumulative_r2 = [0] * n
    for i in range(1, n):
        cumulative_r2[i] = cumulative_r2[i - 1] + r2[i - 1]
    
    possible_scores = [0] * n
    for i in range(n):
        possible_scores[i] = max(cumulative_r1[i], cumulative_r2[i])
    
    print(min(possible_scores))