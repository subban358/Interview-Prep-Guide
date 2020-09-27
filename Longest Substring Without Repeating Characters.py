class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
        
        start, end = 0, 0
        currLen, maxLen = 0, 0
        
        seen = set()
        
        while end < len(s):
            
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
                maxLen = max(maxLen, end - start)
            else:
                seen.remove(s[start])
                start += 1
            
        
        return maxLen
