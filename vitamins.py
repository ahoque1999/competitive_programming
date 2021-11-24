n = int(input())
s = []
c = []

for iteration in range(n):
    temp_c, temp_s = input().split()
    s.append(temp_s)
    c.append(int(temp_c))

A = []
A_found = False
for index in range(n):
    if s[index] == "A":
        A.append(c[index])
if A != []:
    A_found = True
    min_A = min(A)

B = []
B_found = False
for index in range(n):
    if s[index] == "B":
        B.append(c[index])
if B != []:
    B_found = True
    min_B = min(B)

C = []
C_found = False
for index in range(n):
    if s[index] == "C":
        C.append(c[index])
if C != []:
    C_found = True
    min_C = min(C)

AB = []
AB_found = False
for index in range(n):
    if s[index] == "AB" or s[index] == "BA":
        AB.append(c[index])
if AB != []:
    AB_found = True
    min_AB = min(AB)

AC = []
AC_found = False
for index in range(n):
    if s[index] == "AC" or s[index] == "CA":
        AC.append(c[index])
if AC != []:
    AC_found = True
    min_AC = min(AC)

BC = []
BC_found = False
for index in range(n):
    if s[index] == "BC" or s[index] == "CB":
        BC.append(c[index])
if BC != []:
    BC_found = True
    min_BC = min(BC)

ABC = []
ABC_found = False
for index in range(n):
    if len(s[index]) == 3:
        ABC.append(c[index])
if ABC != []:
    ABC_found = True
    min_ABC = min(ABC)

# candidates 
# can be 
candidates = []

# A and B and C
if A_found and B_found and C_found:
    candidates.append(min_A + min_B + min_C)

# A and BC
if A_found and BC_found:
    candidates.append(min_A + min_BC)

# B and AC
if B_found and AC_found:
    candidates.append(min_B + min_AC)

# C and AB
if C_found and AB_found:
    candidates.append(min_C + min_AB)

# AC and AB
if AC_found and AB_found:
    candidates.append(min_AC + min_AB)

# BC and AB
if BC_found and AB_found:
    candidates.append(min_BC + min_AB)

# BC and AC
if BC_found and AC_found:
    candidates.append(min_BC + min_AC)

# ABC
if ABC_found:
    candidates.append(min_ABC)

print(min(candidates)) if candidates != [] else print(-1)