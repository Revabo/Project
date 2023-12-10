import sys
sys.setrecursionlimit(10**9)

N, M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(sys.stdin.readline().strip())

visited = [[0 for _ in range(M)] for __ in range(N)]
result = [[1 for _ in range(M)] for __ in range(N)]
queue = []

def Maze():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '1':
                if visited[i][j] == 0:
                    BFS(i,j)
                    visited[i][j] = 1
    return result[N-1][M-1]
                    
def BFS(x,y):
    queue.append((x,y))
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            my = y + dy[i]
            
            if nx < 0 or nx >= N or my < 0 or my >= M:
                continue
            else:
                if visited[nx][my] == 0 and graph[nx][my] == '1':
                    queue.append((nx,my))
                    visited[nx][my] = 1
                    result[nx][my] = result[x][y] + 1

if __name__ == '__main__':
    print(Maze())