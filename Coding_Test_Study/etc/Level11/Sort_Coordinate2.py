import sys

a = int(sys.stdin.readline())
b = [[0,0] for _ in range(a)]
for i in range(a):
    b[i] = list(map(int,sys.stdin.readline().split()))
    tmp = b[i][0]
    b[i][0] = b[i][1]
    b[i][1] = tmp
b.sort()
for i in range(a):
    print(b[i][1],b[i][0],sep=' ')