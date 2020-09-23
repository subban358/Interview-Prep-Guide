class Solution:
    def kadane(self, num):
        res, curr = num[0], num[0]
        for i in num[1:]:
            curr = max(i, i+curr)
            res = max(res, curr)
        return res    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        K = self.kadane(A)
        cs = 0
        for i in range(len(A)):
            cs += A[i]
            A[i] *= -1
        cs = cs + self.kadane(A)
        
        if cs > K and cs != 0:
            return cs
        else:
            return K
            
        
