from math import ceil

t = int(input())
for i in range(t) :
    a, b, n = map(int,input().split())
    if n%a != 0 : floor = n%a
    else : floor = a
    print(floor,format(ceil(n/a), '02'),sep='')