for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    t = []
    for i in range(0, (n*2)-1, 2):
        t.append([l[i], l[i+1]])
    t.sort(key=lambda x:x[0])
    i = 1
    while i < len(t):
        if t[i][0] <= t[i-1][1]:
            t[i-1][0] = min(t[i-1][0], t[i][0])
            t[i-1][1] = max(t[i-1][1], t[i][1])
            t.pop(i)
        else:
            i+=1
    for i in t:
        for j in i:
            print(j,end=" ")        
    print()        
##############################################################

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key =  lambda x : x[0])
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
