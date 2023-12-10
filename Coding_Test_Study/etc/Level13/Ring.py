import math

a = int(input())
b = list(map(int,input().split()))
gcd = [0]*a
for i in range(1,a):
    gcd[i] = math.gcd(b[i],b[0])
    print(b[0]//gcd[i],'/',b[i]//gcd[i],sep='')