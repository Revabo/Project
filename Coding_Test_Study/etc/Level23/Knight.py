import sys

n = int(sys.stdin.readline())

def Knight():
    for i in range(n):
        a = int(sys.stdin.readline())
        knight = list(map(int,sys.stdin.readline().split()))
        target = list(map(int,sys.stdin.readline().split()))
        print(BFS(a,knight,target))

def BFS(a,knight,target):
    visited = [[0 for i in range(a+1)] for j in range(a+1)]
    result = [[0 for i in range(a+1)] for j in range(a+1)]
    queue = []
    visited[knight[0]][knight[1]] = 1
    queue.append([knight[0],knight[1]])
    dx = [-2,-1,1,2,-2,-1,1,2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    
    while(queue):
        x, y = queue.pop(0)
        for i in range(8):
            cx = x + dx[i]
            cy = y + dy[i]
            
            if cx < 0 or cx >= a or cy < 0 or cy >= a:
                continue
                
            if visited[cx][cy] == 0:
                visited[cx][cy] = 1
                queue.append([cx,cy])
                result[cx][cy] = result[x][y] + 1
                
    return result[target[0]][target[1]]
    
    
if __name__ == '__main__':
    Knight()