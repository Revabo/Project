import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[0 for i in range(n)] for i in range(n)]
sum = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            sum[i][j] == arr[i][j]
        if i == 0 :
            sum[i][j] = arr[i][j] + sum[i][j-1]
        elif j == 0:
            sum[i][j] = arr[i][j] + sum[i-1][j]
        else:
            sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + arr[i][j]
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    
    if x1 == 0 and y1 == 0:
        result = sum[x2][y2]
    elif x1 == 0:
        result = sum[x2][y2] - sum[x2][y1-1]
    elif y1 == 0:
        result = sum[x2][y2]- sum[x1-1][y2]
    else:
        result = sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1]
    print(result)
    