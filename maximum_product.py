for iteration in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    sorted_a = sorted(a)

    product_list = []

    # make sliding window that goes from last 5 to first 5
    first_pos = []
    second_pos = []
    third_pos = []
    fourth_pos = []
    fifth_pos = []
    for iteration in range(5):
        first_pos.append((n - 5 + iteration) % n)
        second_pos.append((n - 4 + iteration) % n)
        third_pos.append((n - 3 + iteration) % n)
        fourth_pos.append((n - 2 + iteration) % n)
        fifth_pos.append((n - 1 + iteration) % n)

        product_list.append(sorted_a[first_pos[iteration]] * sorted_a[second_pos[iteration]] * sorted_a[third_pos[iteration]] * sorted_a[fourth_pos[iteration]] * sorted_a[fifth_pos[iteration]])
    
    print(max(product_list))