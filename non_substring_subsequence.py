def match(char, encode):
    if encode == 3:
        return True
    elif char == "1" and encode == 1:
        return True
    elif char == "0" and encode == 2:
        return True
    else:
        return False

for i in range(int(input())):
    n, q = list(map(int, input().split()))
    s = input()
    reverse_s = s[::-1]

    encode_left = [0] * n
    encode_left[1] = 1 if s[0] == "1" else 2
    for i in range(2, n):
        if encode_left[i - 1] == 3:
            encode_left[i] = 3
        else:
            encode_left[i] = 3 if s[i - 1] != s[i - 2] else encode_left[i - 1]

    encode_right = [0] * n
    encode_right[1] = 1 if reverse_s[0] == "1" else 2
    for i in range(2, n):
        if encode_right[i - 1] == 3:
            encode_right[i] = 3
        else:
            encode_right[i] = 3 if reverse_s[i - 1] != reverse_s[i - 2] else encode_right[i - 1]    
    encode_right = encode_right[::-1]

    for i in range(q):
        l, r = list(map(int, input().split()))
        left_char = s[l - 1]
        right_char = s[r - 1]
    
        print("YES") if match(left_char, encode_left[l - 1]) or match(right_char, encode_right[r - 1]) else print("NO")