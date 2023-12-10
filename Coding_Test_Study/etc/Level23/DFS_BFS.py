import sys

n, m, r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    v, u = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visitedD = [False] * (n+1)
visitedB = [False] * (n+1)
resultD = [0] * (n+1)
resultB = [0] * (n+1)
queue = []
count = 1

def DFS(r):
    global count
    visitedD[r] = True
    resultD[count] = r
    graph[r].sort()
    for node in graph[r]:
        if visitedD[node] == False:
            count += 1
            DFS(node)

def BFS():
    count = 1
    visitedB[r] = True
    resultB[count] = r
    count += 1
    queue.append(r)
    while(queue):
        cur = queue.pop(0)
        graph[cur].sort()
        for node in graph[cur]:
            if visitedB[node] == False:
                visitedB[node] = True
                queue.append(node)
                resultB[count] = node
                count += 1
                
if __name__ == '__main__':
    DFS(r)
    for i in range(1,n+1):
        if resultD[i] == 0:
            continue
        print(resultD[i],end=' ')
    print('')
    BFS()
    for i in range(1,n+1):
        if resultB[i] == 0:
            continue
        print(resultB[i],end=' ')