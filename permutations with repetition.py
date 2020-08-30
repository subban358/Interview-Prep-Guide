class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = [None] * len(nums)
        ans = []
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
                
        keys = list(d.keys())
        vals = list(d.values())
        
        self.helper(keys, vals, res, 0, ans)
        return ans

    def helper(self, keys, vals, res, level, ans):
        
        if level == len(res):
            temp = list(res)
            ans.append(temp)
            return 
        
        for i in range(len(keys)):
            if vals[i] == 0:
                continue
            res[level] = keys[i]
            vals[i] -= 1
            self.helper(keys, vals, res, level + 1, ans)
            vals[i] += 1
        
