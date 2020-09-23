def givenSumSubArr(l, n, ans):
    start, end = 0, 0
    currSum = l[0]
    while end < n:
        if currSum > target and start <= end:
            currSum -= l[start]
            start += 1
        
        if currSum == target:
            ans.append(start+1)
            ans.append(end+1)
            return True
        if currSum < target:
            end += 1
            if end < n: currSum += l[end]
        
    return False

for _ in range(int(input())):
    n, target = map(int, input().split())
    l = [int(x) for x in input().split()]
    ans = []
    
    if givenSumSubArr(l, n, ans):
        print(*ans)
    else:
        print(-1)
    
            
            
        
