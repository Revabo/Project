import sys
import math

a = int(input())
b = list()
c = [0]*8001
cnt = 0
for i in range(a):
    tmp = int(sys.stdin.readline())
    b.append(tmp)
    c[tmp+4000] += 1
b.sort()
print(round(sum(b)/a))

print(b[math.floor(a/2)])

tmp = max(c)
if c.count(tmp) > 1: 
    for i in range(8001):
        if c[i] == tmp:
            cnt += 1
            if cnt == 2:
                tmp = i-4000
                break
else : tmp = c.index(max(c))-4000
print(tmp)

print(max(b)-min(b))