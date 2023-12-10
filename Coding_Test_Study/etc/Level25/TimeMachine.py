import sys
n, m = map(int,sys.stdin.readline().split())
graph = []
Dist = [10000000 for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph.append((a,b,c))
    
def Time_machine():
    Dist[1] = 0
    for i in range(n):
        for j in range(m):
            node = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]
            if Dist[node] != 10000000 and Dist[next_node] > Dist[node] + cost:
                Dist[next_node] = Dist[node] + cost
                if i == n-1:
                    return True
    return False
        
    
if __name__ == '__main__':
    Bool = Time_machine()
    if Bool:
        print(-1)
    else:
        for i in range(2,n+1):
            if Dist[i] >= 10000000:
                print(-1)
            else:
                print(Dist[i])