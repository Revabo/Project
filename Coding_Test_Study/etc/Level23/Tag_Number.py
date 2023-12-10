import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(n):
    graph[i] = list(sys.stdin.readline().strip())

visited = [[0 for _ in range(n)] for __ in range(n)]
queue = []
tag = []

def Tag():
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1':
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    BFS(i,j,count)
                    count += 1
    print(count)
    return count

def BFS(x,y,count):
    tag.append(1)
    queue.append((x,y))
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            else:
                if visited[nx][ny] == 0 and graph[nx][ny] == '1':
                    tag[count] += 1
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    
if __name__ == '__main__':
    count = Tag()
    tag.sort()
    for i in range(count):
        print(tag[i])