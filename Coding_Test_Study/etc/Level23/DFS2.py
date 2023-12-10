import sys
sys.setrecursionlimit(10**9)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
count = 1
visited = [-1] * (n+1)
result = [0] * (n+1)

def DFS(R):
    global count
    visited[R] = 1
    result[R] = count
    
    graph[R].sort(reverse = True)
    for node in graph[R]:
        if visited[node] == -1:
            count += 1
            DFS(node)
            
    return
    
if __name__ == '__main__':
    DFS(r)
    for i in range(1,n+1):
        print(result[i])