for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    matrix = []
    for i in range(0, n*n, n):
        matrix.append(l[i:n+i])
    size = n-1    
    for layer in range(0, (n//2)):
        for i in range(layer, size-layer):
            top = matrix[layer][i]
            right = matrix[i][size-layer]
            bottom = matrix[size-layer][size-i]
            left = matrix[size-i][layer]
            matrix[layer][i] = right
            matrix[i][size-layer] = bottom
            matrix[size-layer][size-i] = left
            matrix[size-i][layer] = top
    for i in matrix:
        print(*i,end=" ")
    print()    
