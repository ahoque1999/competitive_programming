for i in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    
    largest = max(x)
    smallest =  min(x)
    counts = [0] * (largest + 1)
    x = [xi - smallest + 1 for xi in x]
    for xi in x:
        if counts[xi - 1] == 0: 
            counts[xi - 1] += 1
        elif counts[xi] == 0:
            counts[xi]  += 1

    print(sum(counts)) 