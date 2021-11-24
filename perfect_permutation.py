def print_list(list):
    for ele in list:
        print(ele, end=" ")
    print()

n = int(input())

print_list(list(range(1, n + 1)[::-1])) if n % 2 == 0 else print(-1)