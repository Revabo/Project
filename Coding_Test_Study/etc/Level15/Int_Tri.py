import sys

a = int(sys.stdin.readline())
b = []
c = []
for i in range(a):
    b.append(list(map(int,sys.stdin.readline().split())))
    c.append([0]*(i+1))
    if i == 0:
        c[0] = b[0]
    elif i == 1:
        c[1][0] = b[0][0] + b[1][0]
        c[1][1] = b[0][0] + b[1][1]
    else:
        for j in range(i+1):
            if j == 0:
                c[i][0] = c[i-1][0] + b[i][0]
            elif j == i:
                c[i][j] = c[i-1][j-1] + b[i][j]
            else:
                c[i][j] = max(c[i-1][j-1],c[i-1][j]) + b[i][j]
print(max(c[a-1]))