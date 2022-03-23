for iteration in range(int(input())):
    s = input()
    n = len(s)

    # start index
    start = n -1
    for i in range(n):
        if s[i] == '1':
            start = i
            break
    
    # last index
    end = 0
    for i in range(n-1,-1,-1):
        if s[i] == '1':
            end = i
            break

    s = s[start:end]

    counter  =0
    for char in s:
        if char =='0':
            counter += 1

    print(counter)