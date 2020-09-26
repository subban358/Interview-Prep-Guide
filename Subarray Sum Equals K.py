class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        d = {}
        d[0] = 1
        Sum = 0
        c = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum-k in d:
                c += d[Sum-k]
            if Sum in d:
                d[Sum] += 1

            else:
                d[Sum] = 1
        return c        
