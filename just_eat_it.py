for iteration in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    yassers_score = sum(a)
    adels_score = a[0]
    # kadanes algorithm
    max_ending = 0
    start = -1
    end = 0
    for index in range(n):
        max_ending = max_ending + a[index]
        if max_ending <= 0:
            max_ending = 0
            start = index
        elif adels_score < max_ending:
            adels_score = max_ending
            end = index

    if (end - start) == n:
        print("YES")
    elif adels_score < yassers_score:
        print("YES")
    else:
        print("NO")