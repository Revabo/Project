import sys

a = int(sys.stdin.readline())
b = []
c = [[0,0] for _ in range(a)]
for i in range(a):
    b.append(int(sys.stdin.readline()))
    if i == 0:
        c[0][0] = c[0][1] = b[0]
    elif i == 1:
        c[1][0] = b[0] + b[1]
        c[1][1] = b[1]
    elif i == 2:
        c[i][0] = c[i-1][1] + b[i]
        c[i][1] = max(c[i-2]) + b[i]
    else:
        c[i][0] = c[i-1][1] + b[i]
        c[i][1] = max(max(c[i-2]),max(c[i-3])) + b[i]
print(max(c[a-1][0],c[a-1][1],c[a-2][0],c[a-2][1]))