for iteration in range(int(input())):
    a, b = list(map(int, input().split()))
    string = input()

    num_1s = len([element for element in string.split("0") if element != ""])

    if num_1s == 0:
        print(0)
        continue

    base =  a * num_1s

    length_0s = [len(element) for element in string.split("1") if element != ""]

    if string[0] == "0":
        del length_0s[0]
    if string[-1] == "0":
        del length_0s[-1]

    for length in length_0s:
        change = b * length - a
        if change < 0:
            base += change
    
    print(base)