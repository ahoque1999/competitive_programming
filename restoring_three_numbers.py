list_of_x = list(map(int, input().split()))
sum_3 = max(list_of_x)
list_of_x.remove(sum_3)
for x in list_of_x:
    print(sum_3 - x, end=" ")