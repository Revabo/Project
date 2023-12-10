import sys

a = int(sys.stdin.readline())
b = [[0,'a'] for _ in range(a)]
for i in range(a):
    b[i] = list(sys.stdin.readline().split())
    b[i][0] = int(b[i][0])
b.sort(key = lambda x : x[0])
for i in range(a):
    print(b[i][0],b[i][1],sep=' ')