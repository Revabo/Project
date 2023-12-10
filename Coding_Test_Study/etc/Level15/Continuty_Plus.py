import sys

a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
c = [0]*a

for n in range(a):
    if n == 0:
        c[0] = b[0]
    else:
        tmp = b[n] + c[n-1]
        if tmp >= b[n]:
            c[n] = tmp
        else:
            c[n] = b[n]
print(max(c))