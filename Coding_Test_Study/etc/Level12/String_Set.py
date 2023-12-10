import sys

a = list(map(int,sys.stdin.readline().split()))
b = ['-']*a[0]
cnt = 0
for i in range(a[0]):
    b[i] = sys.stdin.readline().strip()
for i in range(a[1]):
    tmp = sys.stdin.readline().strip()
    if tmp in b :
        cnt += 1
print(cnt)