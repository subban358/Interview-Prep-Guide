mod = 1000000007
def power(a, b):
    if b==0:
        return 1
    else:
        r = power(a, b//2)
        if b % 2 == 0:
            return (r*r)%mod
        else:
            return (r*a*r)%mod
for _ in range(int(input())):
    n = int(input())
    b = int(str(n)[::-1])
    print(power(n, b))
