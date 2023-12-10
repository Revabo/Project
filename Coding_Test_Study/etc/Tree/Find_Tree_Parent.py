import sys
input = sys.stdin.readline

N = int(input())
Tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    Tree[b].append(a)
    Tree[a].append(b)
    
heap = []
visited = [0 for _ in range(N+1)]
heap.append(1)
visited[1] = 1
result = [0 for _ in range(N+1)]
while(heap):
    cur = heap.pop()
    for node in Tree[cur]:
        if visited[node] == 0:
            heap.append(node)
            visited[node] = 1
            result[node] = cur
            
for i in range(2,N+1):
    print(result[i])