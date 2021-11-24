m = []
c =[]
n = int(input())

for i in range(n):
    mi, ci = list(map(int, input().split()))
    m.append(mi)
    c.append(ci)

m_wins = sum([1 for i in range(n) if m[i] > c[i]])
c_wins = sum([1 for i in range(n) if c[i] > m[i]])
if m_wins > c_wins:
    print("Mishka")
elif c_wins > m_wins:
    print("Chris")
else:
    print("Friendship is magic!^^")