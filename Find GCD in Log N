def getGCD(a, b):
    if b == 0: return a
    return getGCD(b, a%b)

for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    if n == 1:
        print(l[0])
    else:    
        gcd = getGCD(l[0], l[1])
        for i in range(2, n):
            gcd = getGCD(gcd, l[i])
        print(gcd)
