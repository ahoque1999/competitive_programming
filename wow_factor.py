#  all os are pivots
# count how many ws preceding each pivot
# count how many ws superceding each pivot
# multiply and add

s = input()
n = len(s)

# define pivot lengths
temp_length = 0
length = []
for i in range(n):
    if i == 0:
        if s[i] == "o":
            temp_length += 1
        continue
    if s[i] == "o":
        temp_length += 1
    if s[i] == "v" and s[i - 1] == "o":
        length.append(temp_length)
        temp_length = 0
if temp_length != 0:
    length.append(temp_length)

# define preceding lengths
pre  = []
temp_pre = 0
cum_pre = 0
for i in range(n):
    if i == 0:
        if s[i] == "o":
            cum_pre += max([temp_pre - 1, 0])
            temp_pre = 0
            pre.append(cum_pre)
            continue
    if s[i] == "v":
        temp_pre += 1
    if s[i] == "o" and s[i - 1] == "v":
        cum_pre += max([temp_pre - 1, 0])
        temp_pre = 0
        pre.append(cum_pre)      

# define superceding lengths
sup = []
temp_sup = 0
cum_sup = 0
rev_s = s[::-1]
for i in range(n):
    if i == 0:
        if rev_s[i] == "o":
            cum_sup += max([temp_sup - 1, 0])
            temp_sup = 0
            sup.append(cum_sup)
            continue
    if rev_s[i] == "v":
        temp_sup += 1
    if rev_s[i] == "o" and rev_s[i - 1] == "v":
        cum_sup += max([temp_sup - 1, 0])
        temp_sup = 0
        sup.append(cum_sup)
sup = sup[::-1]

n = len(length)

total = 0
for i in range(n):
    total += length[i] * pre[i] * sup[i]
print(total)