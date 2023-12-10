import sys

a = list(map(int,sys.stdin.readline().split()))
k = list(map(int,sys.stdin.readline().split()))
x = [0]*a[0]

if a[1] == 1:
    print(max(k))
    exit()

for i in range(1,a[0]):
    k[i] += k[i-1]
for i in range(a[1],a[0]):
    x[i] = k[i] - k[i-a[1]]
print(max(x[a[1]-1:]))