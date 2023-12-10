import sys

a = int(sys.stdin.readline())
b = [[0,0,0,0,0,0,0,0,0,0] for _ in range(a)]
b[0] = [0,1,1,1,1,1,1,1,1,1]
for i in range(1,a):
    for j in range(10):
        if j == 0:
            b[i][j] = b[i-1][1]
        elif j == 9:
            b[i][j] = b[i-1][8]
        else:
            b[i][j] = (b[i-1][j-1] + b[i-1][j+1])
print(sum(b[a-1])%1000000000)