import sys

def GCD(a,b):
    if a%b == 0:
        return b
    elif b == 0:
        return a
    else :
        return GCD(b,a%b)

n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    gcd = GCD(a,b)
    print(a*b//gcd)