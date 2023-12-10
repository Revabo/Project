import sys

n, k = map(int,sys.stdin.readline().split())

if n > k : a = n
elif n == k:
    print(0)
    exit()
else: a = k
    
visited = [0 for _ in range(100001)]
result = [0 for _ in range(100001)]
queue = []
def BFS():
    visited[n] = 1
    queue.append(n)
    while(queue):
        cur = queue.pop(0)
        nodes = [cur-1, cur+1, cur*2]
        for node in nodes:
            if node < 0 or node >= 100001:
                continue
            if visited[node] == 0:
                visited[node] = 1
                queue.append(node)
                result[node] = result[cur] + 1
                if node == k :
                    return result[node]

    
if __name__ == '__main__':
    print(BFS())