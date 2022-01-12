def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a,b):
    prod = a * b
    hcf = gcd (a,b)
    return prod // hcf
t = int(input())
while t:
    m,n = map(int, input().split())
    print("GCD OF NUMBER {} LCM OF NUMBER {}".format(gcd(m,n), lcm(m,n)))
    t = t - 1
