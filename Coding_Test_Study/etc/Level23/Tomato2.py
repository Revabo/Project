import sys
from collections import deque

m, n, h = map(int,sys.stdin.readline().split())
graph = [[[0 for _ in range(m)] for __ in range(n)] for ___ in range(h)]

for i in range(h):
    for j in range(n):
        graph[i][j] = list(map(int,sys.stdin.readline().split()))
    
visited = [[[0 for _ in range(m)] for __ in range(n)] for ___ in range(h)]
result = [[[-1 for _ in range(m)] for __ in range(n)] for ___ in range(h)]
queue = deque()
    
def Tomato():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    visited[i][j][k] = 1
                    result[i][j][k] = 0
                    queue.append([i,j,k])
    BFS()
    
def BFS():
    Max = -10000000000
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    while(queue):
        x, y, z = queue.popleft()
        for i in range(6):
            cx = x + dx[i]
            cy = y + dy[i]
            cz = z + dz[i]
            if cx < 0 or cx >= h or cy < 0 or cy >= n or cz < 0 or cz >= m:
                continue
            if visited[cx][cy][cz] == 0 and graph[cx][cy][cz] != -1:
                visited[cx][cy][cz] = 1
                queue.append([cx,cy,cz])
                result[cx][cy][cz] = result[x][y][z] + 1
        
if __name__ == '__main__':
    Tomato()
    Max = -100000000
    
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if result[i][j][k] == -1 and graph[i][j][k] != -1:
                    print(-1)
                    exit()
                else:
                    Max = max(Max,result[i][j][k])
    print(Max)