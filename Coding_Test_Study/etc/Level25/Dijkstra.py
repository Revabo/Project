import sys
from heapq import heappop, heappush

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
Dist = [100000000 for _ in range(V+1)]
graph = [[] for _ in range(V+1)]
Heap = []

for i in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))

def Short():
    Dist[K] = 0
    heappush(Heap,(0,K))
    while(Heap):
        cur, dist = heappop(Heap)
        for node in graph[cur]:
            cost = Dist[cur] + node[1]
            if Dist[node[0]] > cost:
                Dist[node[0]] = cost
                heappush(Heap,(cost,node[0]))
    
if __name__ == '__main__':
    Short()
    for i in range(1,V+1):
        if Dist[i] != 100000000:
            print(Dist[i])
        else:
            print('INF')