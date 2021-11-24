def number_of_pieces(w, h):
    if w % 2 == 1 and h % 2 == 1:
        return 1
    elif w % 2 == 1:
        return 2 * number_of_pieces(w, h //2) 
    return 2 * number_of_pieces(w // 2, h)

for i in range(int(input())):
    w, h, n = list(map(int, input().split()))
    print("YES") if number_of_pieces(w, h) >= n else print("NO")