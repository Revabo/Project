import sys

a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
c = [0]*a
for i in range(a):
    if i == 0:
        c[0] = 1
    else:
        for j in range(i-1,-1,-1):
            if b[i] > b[j]:
                if c[i] < c[j]:
                    c[i] = c[j]
        c[i] += 1
print(max(c))