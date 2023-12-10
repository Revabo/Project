import sys
input = sys.stdin.readline
INF = 100000000

n = int(input())
m = int(input())
Dist = [[INF for _ in range(n+1)] for __ in range(n+1)]

for i in range(1,n+1):
    Dist[i][i] = 0
    
for i in range(m):
    a,b,c = map(int,input().split())
    Dist[a][b] = min(Dist[a][b], c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            Dist[i][j] = min(Dist[i][j], Dist[i][k] + Dist[k][j])
            
for i in range(1,n+1):
    for j in range(1,n+1):
        if Dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(Dist[i][j],end=' ')
    print('')