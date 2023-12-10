import sys
from collections import deque

m, n = map(int,sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    
visited = [[0 for _ in range(m+1)] for __ in range(n+1)]
result = [[-1 for _ in range(m+1)] for __ in range(n+1)]
queue = deque([])

def Tomato():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                visited[i][j] = 1
                result[i][j] = 0
                queue.append([i,j])
    BFS(queue)

def BFS(queue):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if cx < 0 or cx >= n or cy < 0 or cy >= m:
                continue
                
            if visited[cx][cy] == 0 and graph[cx][cy] != -1:
                queue.append([cx,cy])
                visited[cx][cy] = 1
                result[cx][cy] = result[x][y] + 1
    
    
if __name__ == '__main__':
    Tomato()
    Max = -10000000
    for i in range(n):
        for j in range(m):
            if result[i][j] == -1 and graph[i][j] != -1:
                print(-1)
                exit()
            Max = max(Max,result[i][j])
    print(Max)             