class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        
        if n <= 1:
            return 1
        if n == 2 and A[0] != A[1]:
            return n
        
        checkpoint = 0
        ans = 1
        
        def cmp(a, b):
            if a == b:
                return 0
            if a > b:
                return 1
            return -1
        
        for i in range(1, n):
            sign = cmp(A[i-1], A[i])
            
            if sign == 0:
                checkpoint = i
            
            elif i == n-1 or sign * cmp(A[i], A[i+1]) != -1:
                ans = max(ans, i - checkpoint + 1)
                checkpoint = i
        
        return ans
