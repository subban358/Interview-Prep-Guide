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

    
###########################################################################
    
class Solution:
    def reverse(self, nums):
        l, r = 0, len(nums)-1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
    def rotate(self, A):
        n = len(A)
        for i in range(0, n):
            for j in range(i, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for row in A:
            self.reverse(row)
        return A
