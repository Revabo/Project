import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(m):
    v, u = map(int,sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

visited = [False] * (n+1)
queue = []
def DFS():
    count = 0
    visited[1] = True
    queue.append(1)
    while(queue):
        cur = queue.pop(0)
        for node in graph[cur]:
            if visited[node] == False:
                visited[node] = True
                count += 1
                queue.append(node)
    return count

if __name__ == '__main__':
    print(DFS())