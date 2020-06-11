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
