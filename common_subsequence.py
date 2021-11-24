for i in range(int(input())):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    check = False
    for bi in b:
        if bi in a:
            check = True
            c = bi
            break
    
        
    print(f"YES\n1 {c}") if check else print("NO") 