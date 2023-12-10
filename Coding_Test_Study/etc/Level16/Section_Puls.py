import sys

a = list(map(int,sys.stdin.readline().split()))
n = list(map(int,sys.stdin.readline().split()))
for i in range(1,a[0]):
    n[i] += n[i-1]
n.insert(0,0)
for i in range(a[1]):
    m = list(map(int,sys.stdin.readline().split()))
    print(n[m[1]]-n[m[0]-1])