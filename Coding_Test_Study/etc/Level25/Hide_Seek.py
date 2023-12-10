import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(100001)]
visited = [0 for _ in range(100001)]
result = [1000000 for _ in range(100001)]
heap = deque([])

def Seek():
    visited[n] = 1
    result[n] = 0
    heap.append(n)
    while(heap):
        x = heap.popleft()
        dx = [x+1,x-1,x*2]
        for i in range(3):
            cx = dx[i]
            if cx < 0 or cx > 100000:
                continue
            if visited[cx] == 0:
                visited[cx] = 1
                heap.append(cx)
                if i == 2:
                    result[cx] = result[x]
                else:
                    result[cx] = result[x] + 1
            elif visited[cx] == 1 and result[cx] > result[x]:
                heap.append(cx)
                if i == 2:
                    result[cx] = result[x]
                else:
                    result[cx] = result[x] + 1
    return result[k]
    
if __name__ == '__main__':
    print(Seek())