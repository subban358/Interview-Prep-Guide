class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        currProd = 1
        count = 0
        
        start, end = 0, 0
        c = 0
        
        while end < len(nums):
            currProd *= nums[end]
            while currProd >= k:
                currProd //= nums[start]
                start += 1
            count += end - start + 1
            end += 1
        
        return count + c
