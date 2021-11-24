def sol1():
    n, k = list(map(int, input().split()))
    s = input()
    c = input().split()

    flagged_indices =[]
    for index in range(n):
        if s[index] not in c:
            flagged_indices.append(index)

    reductions = 0
    for substring_length in range(1, n + 1):
        for start in range(n - substring_length + 1):
            for index in flagged_indices:
                if start <= index <= start + substring_length - 1:
                    reductions += 1
                    break

    print(n * (n + 1) // 2 - reductions)

def sol2():
    n, k = list(map(int, input().split()))
    s = input()
    c = input().split()

    start = []
    end = []

    # encoding
    encoded = [0] * n
    for index in range(n):
        if s[index] in c:
            encoded[index] = 1

    if encoded[0] == 1:
        start.append(0) 

    # get start indices
    for index in range(1, n):
        if encoded[index] == 1 and encoded[index - 1] == 0:
            start.append(index)

    # get end indices
    for index in range(n - 1):
        if encoded[index] == 1 and encoded[index + 1] == 0:
            end.append(index)

    if encoded[n - 1] == 1:
        end.append(n - 1)
    
    # get lengths[index] = end[index] - start[index] + 1
    number_of_contiguous_substrings = len(start)
    lengths = [end[index] - start[index] + 1 for index in range(number_of_contiguous_substrings)]

    total = 0
    for index in range(number_of_contiguous_substrings):
        combinations = lengths[index] * (lengths[index] + 1) // 2
        total += combinations 
    
    print(total)

sol2()