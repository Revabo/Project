import sys
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for i in range(V):
    tmp = list(map(int,input().split()))
    v = tmp[0]
    for j in range(1,len(tmp)-1,2):
        graph[v].append((tmp[j],tmp[j+1]))

def BFS(v):
    visited = [0 for _ in range(V+1)]
    result = [0 for _ in range(V+1)]
    heap = []
    Max = (-1,0)
    heap.append(v)
    visited[v] = 1
    while(heap):
        cur = heap.pop()
        for node, dist in graph[cur]:
            if visited[node] == 0:
                visited[node] = 1
                result[node] = result[cur] + dist
                heap.append(node)
                if Max[0] < result[node]:
                    Max = (result[node],node)
    return Max
                
Max, v = BFS(1)
Max, v = BFS(v)
print(Max)