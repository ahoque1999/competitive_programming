def check(s_):
    n = len(s_)
    start = 0
    end = n - 1
    for i in range((ord('a') + n - 1), ord('a') - 1, -1):
        temp_s = s_[start:end + 1]
        if temp_s[0] == chr(i):
            start = start + 1
        elif temp_s[-1] == chr(i):
            end = end - 1
        else:
            return False
    return True


for _ in range(int(input())):
    s = input()
    print("YES") if check(s) else print("NO")