dict = {"Tetrahedron" : 4,
        "Cube" : 6,
        "Octahedron" : 8,
        "Dodecahedron" : 12,
        "Icosahedron" : 20}

n = int(input())
sum = 0
for i in range(n):
    sum += dict[input()]
print(sum)