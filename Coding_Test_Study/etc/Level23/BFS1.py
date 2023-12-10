import sys

n, m, r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (n+1)
queue = []
result = [0] * (n+1)
    
def BFS():
    
    count = 1
    visited[r] = True
    queue.append(r)
    result[r] = count
    count += 1
    
    while(queue):
        cur = queue.pop(0)
        graph[cur].sort(reverse = True)
        for node in graph[cur]:
            if visited[node] == False:
                visited[node] = True
                queue.append(node)
                result[node] = count
                count += 1
                
if __name__ == '__main__':
    BFS()
    for i in range(1,n+1):
        print(result[i])