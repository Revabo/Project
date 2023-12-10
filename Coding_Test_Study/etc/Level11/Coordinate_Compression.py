import sys

a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
c = list(set(b))
c.sort()
d = {c[i] : i for i in range(len(c))}
for i in range(a):
    print(d[b[i]],end=' ')