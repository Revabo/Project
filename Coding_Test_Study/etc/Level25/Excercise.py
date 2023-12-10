import sys
input = sys.stdin.readline

INF = 1000000000
V,E = map(int,input().split())
Dist = [[INF for _ in range(V+1)] for __ in range(V+1)]

for i in range(E):
    a,b,c = map(int,input().split())
    Dist[a][b] = c

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if Dist[i][j] > Dist[i][k] + Dist[k][j]:
                Dist[i][j] = Dist[i][k] + Dist[k][j]
            
Min = INF + 1

for i in range(1,V+1):
    Min = min(Min,Dist[i][i])

if Min >= INF:
    print(-1)
else:
    print(Min)