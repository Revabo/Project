import sys
from collections import deque

k = int(sys.stdin.readline())

def Two():
    for i in range(k):
        V, E = map(int,sys.stdin.readline().split())
        print(BFS(V,E))
    
def BFS(V, E):
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    queue = deque()
    for i in range(E):
        u, v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    visited[1] = 1
    queue.append(1)
    while(queue):
        cur = queue.popleft()
        color = visited[cur]
        graph[cur].sort()
        for node in graph[cur]:
            if visited[node] == 0:
                if color == 1:
                    visited[node] = 2
                else:
                    visited[node] = 1
                queue.append(node)
            elif visited[node] == visited[cur]:
                return 'NO'
    return 'YES'

    
if __name__ == '__main__':
    Two()