import sys
from collections import deque

T = int(sys.stdin.readline())

def BFS(L, x, y, N, M):
    L[x][y] = 0
    queue = deque()
    queue.append((x,y))
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            my = y + dy[i]
            
            if nx < 0 or nx >= N or my < 0 or my >= M:
                continue
            else:
                if L[nx][my] == 1:
                    L[nx][my] = 0
                    queue.append((nx,my))
    return

def Organic_Cabbage():
    for i in range(T):
        Count = 0
        N, M, K = map(int, sys.stdin.readline().split())
        L = [[0 for _ in range(M)] for __ in range(N)]
        
        for j in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            L[X][Y] = 1
        
        for n in range(N):
            for m in range(M):
                if L[n][m] == 1:
                    BFS(L, n, m, N, M)
                    Count += 1
        print(Count)
if __name__ == '__main__':
    Organic_Cabbage()