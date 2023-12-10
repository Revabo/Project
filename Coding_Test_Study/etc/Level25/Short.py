import sys
from heapq import heappop, heappush

n, e = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
heap = []

for i in range(e):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

u, v = map(int,sys.stdin.readline().split())

def Short(Start):
    Dist = [1000000000 for _ in range(n+1)]
    Dist[Start] = 0
    heappush(heap,(0,Start))
    while(heap):
        dist, cur = heappop(heap)
        for node in graph[cur]:
            cost = Dist[cur] + node[1]
            if Dist[node[0]] > cost:
                Dist[node[0]] = cost
                heappush(heap,(cost,node[0]))
    return Dist
    
if __name__ == '__main__':
    Dist1 = Short(1)
    Dist2 = Short(u)
    Dist3 = Short(v)
    V1 = Dist1[u] + Dist2[v] + Dist3[n] 
    V2 = Dist1[v] + Dist3[u] + Dist2[n]
    result = min(V1,V2)
    if result >= 1000000000 :
        print(-1)
    else:
        print(result)