# O(n3) solution
def sol1():
    n = int(input())
    a = list(map(int, input().split()))

    lengths = []
    for i in range(n):
        for j in range(i, n):
            temp_a = [a[i] for i in range(n)]
            for k in range(i, j + 1):
                temp_a[k] = 1 - temp_a[k] 
                lengths.append(sum(temp_a))

    print(max(lengths))

def flip(list, left, right):
    temp_list = [ele for ele in list]
    for i in range(left, right + 1):
        temp_list[i] = 1 - temp_list[i]
    for ele in temp_list:
        print(ele, end=" ")
    print()

# O(n2) solution
def sol2():
    def print_list(list, end_list):
        for newvariable388 in list:
            print(newvariable388, end=" ")
        if end_list:
            print()

    def flipped(list):
        return [1 - element for element in list]

    n = int(input())
    s = list(map(int, input().split()))
    cumulative = [0] * (n + 1)
    for start in range(1, n + 1):
        cumulative[start] += cumulative[start - 1] + s[start - 1]

    number_of_ones = []
    total = 0
    for substring_length in range(1, n + 1):
        for start in range(n - substring_length + 1):
            # if preceding element exists
            if start != 0:
                total += cumulative[start]
                # print_list(s[:start], False)
            
            # if superceding element exists
            # normally the line considering the substring can be put here instead of separately into each if else block
            # this was done because the substring acts differently based on the existence of the superceding string apropos to printing
            if start + substring_length - 1 != n - 1:
                total += substring_length - (cumulative[start + substring_length] - cumulative[start])
                # print_list(flipped(s[start : start + substring_length]), False)

                total += cumulative[n] - cumulative[start + substring_length]
                # print_list(s[start + substring_length :], True)
            
            # if superceding element does not exist
            else:
                total += substring_length - (cumulative[start + substring_length] - cumulative[start])
                # print_list(s[start : start + substring_length], True)
            # print(total)
            # print()
            number_of_ones.append(total)
            total = 0

    print(max(number_of_ones))

sol2()