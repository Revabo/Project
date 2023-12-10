import sys

n = int(sys.stdin.readline())
L = [[] for _ in range(n)]
for i in range(n):
    L[i] = list(sys.stdin.readline().rstrip())
result = ''

def Quad_Tree(x,y,n):
    global result
    for i in range(x,x+n):
        for j in range(y,y+n):
            if L[x][y] != L[i][j]:
                n = n // 2
                result += '('
                Quad_Tree(x,y,n)
                Quad_Tree(x,y+n,n)
                Quad_Tree(x+n,y,n)
                Quad_Tree(x+n,y+n,n)
                result += ')'
                return
    
    if L[x][y] == '1':
        result += '1'
    else:
        result += '0'
    
if __name__ == '__main__':
    Quad_Tree(0,0,n)
    print(result)