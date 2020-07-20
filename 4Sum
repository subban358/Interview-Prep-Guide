class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0 or nums == None: return []
        nums.sort()
        ans = []
        length = len(nums)
        i = 0
        while i < length:
            j = i + 1
            while j < length:
                left, right = j + 1, length - 1
                while left < right:
                    currentSum = nums[i] + nums[j] + nums[left] + nums[right] 
                    if currentSum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        leftVal = nums[left]
                        while left < right and nums[left+1] == leftVal:
                            left += 1
                        rightVal = nums[right]
                        while left < right and nums[right-1] == rightVal:
                            right -= 1
                        left += 1
                        right -= 1
                    elif currentSum > target:
                        right -= 1
                    else:
                        left += 1
                while j+1 < length and nums[j+1] == nums[j]: j+=1
                j += 1
            while i+1 < length and nums[i+1] == nums[i]: i+=1
            i += 1
        return ans
                    
