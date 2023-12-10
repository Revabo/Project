import math

def fac(a,b):
    return math.factorial(a)//(math.factorial(a-b)*math.factorial(b))

n = int(input())
for i in range(n):
    a = list(map(int,input().split()))
    print(fac(a[0],a[1])%1000000007)