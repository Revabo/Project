import math

a = int(input())
for i in range(a):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    if x1 == x2 and y1 == y2 and r1 == r2 : 
        print(-1)
        continue
    elif r1 == 0 or r2 == 0 :
        print(0)
        continue
    len = math.sqrt((x2-x1)**2 + (y2-y1)**2) 
    if len == (r1+r2) or abs(r2-r1) == len: print(1)
    elif len < (r1+r2) and (x1 != x2 or y1 != y2) and (len+r1 > r2 and len+r2 > r1): print(2)
    else : print(0)