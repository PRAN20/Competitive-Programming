def sum1(n):     # O[1]
    return (n)*(n+1) // 2

def sum2(n):
    sm = 0       #O[N]
    for i in range (1, n+1):
        sm = sm + i
    return sm
t = int(input())
while t:
    n = int(input())
    print("Executed Sum 1 {}".format(sum1(n)))
    print("Executed Sum 2 {}".format(sum2(n)))
    t = t - 1
