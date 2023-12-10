import sys

a = int(sys.stdin.readline())
b = [[0,0,0] for _ in range(a)]
c = [[0,0,0] for _ in range(a)]
flag = 0
for i in range(a):
    b[i] = list(map(int,sys.stdin.readline().split()))
    if i == 0:
        c[0] = b[0]
    else:
        for j in range(3):
            if j == 0:
                c[i][0] = min(c[i-1][1],c[i-1][2]) + b[i][0]
            elif j == 1:
                c[i][1] = min(c[i-1][0],c[i-1][2]) + b[i][1]
            else:
                c[i][2] = min(c[i-1][0],c[i-1][1]) + b[i][2]
print(min(c[a-1]))