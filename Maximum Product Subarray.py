class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = nums[0], nums[0]
        prvMax, prvMin = nums[0], nums[0]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            currMax = max(nums[i], prvMax*nums[i], prvMin*nums[i])
            currMin = min(nums[i], prvMax*nums[i], prvMin*nums[i])
            
            ans = max(ans, currMax)
            
            prvMax, prvMin = currMax, currMin
        
        return ans
