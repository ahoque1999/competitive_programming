for iteration in range(int(input())):
    s = input()
    uniques = list(set(s))
    frequency = [sum([1 for char in s if char is unique]) for unique in uniques]
    truncated_list = [min(ele, 2) for ele in frequency]
    print(sum(truncated_list) // 2)