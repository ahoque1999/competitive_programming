for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    required_a = min(a)
    required_b = min(b)

    moves = 0
    for i in range(n):
        move_combined = min([a[i] - required_a, b[i] - required_b])
        move_a = a[i] - move_combined - required_a
        move_b = b[i] - move_combined - required_b
        moves += move_combined + move_a + move_b
    
    print(moves)