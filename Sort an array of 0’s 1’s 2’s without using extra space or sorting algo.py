for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    c0, c1, c2 = 0, 0, 0
    for i in arr:
        if i == 0:
            c0+=1
        elif i==1:
            c1+=1
        else:
            c2+=1
    i = 0
    while c0:
        arr[i] = 0
        c0 -= 1
        i+=1
    while c1:
        arr[i] = 1
        c1-=1
        i+=1
    while c2:
        arr[i] = 2
        c2-=1
        i+=1
    print(*arr)    
        
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, curr = 0, len(nums)-1, 0
        while curr <= r:
            if nums[curr] == 0:
                nums[curr], nums[l] = nums[l], nums[curr]
                curr+=1
                l+=1
            elif nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
            else:
                curr += 1
