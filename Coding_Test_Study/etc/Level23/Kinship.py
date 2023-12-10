import sys

n = int(sys.stdin.readline())
a,b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
result = [-1] * (n+1)
queue = []

def BFS():
    visited[a] = True
    result[a] = 0
    queue.append(a)
    while(queue):
        cur = queue.pop(0)
        for node in graph[cur]:
            if visited[node] == False:
                visited[node] = True
                queue.append(node)
                result[node] = result[cur] + 1
    
if __name__ == '__main__':
    BFS()
    #print(result)
    print(result[b])