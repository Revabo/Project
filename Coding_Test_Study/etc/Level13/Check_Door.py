import math

a = int(input())
b = list()
gcd = 0
c = list()
for i in range(a):
    b.append(int(input()))
    if i == 1:
        gcd = abs(b[1] - b[0])
    gcd = math.gcd(gcd, abs(b[i] - b[i-1]))

tmp = round((gcd)**(1/2))
for i in range(2,tmp+1):
    if gcd%i == 0:
        c.append(i)
        c.append(gcd//i)
c.append(gcd)
c = list(set(c))
c.sort()
for i in range(len(c)):
    print(c[i],end=' ')