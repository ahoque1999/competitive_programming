for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    sum_a = sum(a)
    if sum(a) % 2 == 1:
        print("NO")
    elif sum(a) // n == 2 and n % 2 == 1:
        print("NO")
    else:
        print("YES")

def print_result(value_of_sum_a, value_of_n):
    print("NO") if value_of_sum_a % 2 == 1  else print("YES")



