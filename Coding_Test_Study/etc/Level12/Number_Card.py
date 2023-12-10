import sys

a = int(sys.stdin.readline())
b = [0]*20000001
tmp = list(map(int,sys.stdin.readline().split()))
for i in range(a):
     b[tmp[i]+10000000] = 1
c = int(sys.stdin.readline())
d = list(map(int,sys.stdin.readline().split()))
for i in range(c):
    print(b[d[i]+10000000],end=' ')