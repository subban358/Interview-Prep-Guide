class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        partitionList = []
        
        lastSeen = [-1] * 26
        
        for i in range(0, len(S)):
            lastSeen[ord(S[i])-ord('a')] = i
        start, end = 0, 0
        for i in range(len(S)):
            end = max(end, lastSeen[ord(S[i]) - ord('a')])
            if i == end:
                partitionList.append(end-start+1)
                start = end+1
        
        return partitionList
