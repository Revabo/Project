import sys

a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
c = [0]*20000001
for i in range(a):
    c[b[i]+10000000] += 1
d = int(sys.stdin.readline())
e = list(map(int,sys.stdin.readline().split()))
for i in range(d):
    print(c[e[i]+10000000],end=' ')