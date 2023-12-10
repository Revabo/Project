import sys

n = int(sys.stdin.readline())
a  = []
b = [1]*n
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
a.sort()
for i in range(1,n):
    for j in range(i):
        if a[j][1] < a[i][1]:
            tmp = b[j] + 1
            if tmp > b[i]:
                b[i] = tmp
print(n - max(b))