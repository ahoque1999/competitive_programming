def return_number_of_2s(number):
    if number <= 2:
        return 0
    else:
        return 1 + return_number_of_2s(number / 2)

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum([return_number_of_2s(max([a[i + 1], a[i]]) / min([a[i + 1], a[i]])) for i in range(n -1)]))