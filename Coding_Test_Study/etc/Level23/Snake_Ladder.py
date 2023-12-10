import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(101)]

for i in range(n+m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)

visited = [0 for _ in range(101)]
result = [0 for _ in range(101)]
queue = deque()
    
def BFS():
    visited[1] = 1
    queue.append(1)
    dx = [1,2,3,4,5,6]
    while(queue):
        x = queue.popleft()
        if graph[x]:
            cx = graph[x][0]
            if visited[cx] == 0:
                queue.append(cx)
                visited[cx] = 1
                result[cx] = result[x]
            elif result[cx] > result[x]:
                queue.append(cx)
                result[cx] = result[x]
            else: continue
                
        else:
            for i in range(6):
                cx = x + dx[i]
                if cx < 0 or cx >= 101:
                    continue
                if visited[cx] == 0:
                    queue.append(cx)
                    visited[cx] = 1
                    result[cx] = result[x] + 1
                elif result[cx] > (result[x] + 1):
                    queue.append(cx)
                    result[cx] = result[x] + 1
    return result[100]
    
if __name__ == '__main__':
    print(BFS())