n, m = list(map(int, input().split()))
print('#'*m)
for i in range(n // 2): 
    print('.' * (m - 1) + '#') if i % 2 == 0 else print('#' + '.' * (m - 1))
    print('#' * m)