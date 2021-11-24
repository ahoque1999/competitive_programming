list_iter = iter(input())
for i in list_iter:
    if i == "-":
        check = next(list_iter, None)
        print(2, end="") if check == "-" else print(1, end="")
    else:
        print(0, end="")