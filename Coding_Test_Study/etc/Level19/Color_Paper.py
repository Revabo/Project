import sys

n = int(sys.stdin.readline())
result_zero = 0
result_one = 0
L = [[] for _ in range(n)]
for i in range(n):
    L[i] = list(map(int,sys.stdin.readline().split()))
print(L)
    
def Color_Paper(x,y,n):
    global result_one, result_zero
    for i in range(x,x+n):
        for j in range(y,y+n):
            if L[x][y] != L[i][j]:
                n = n // 2
                Color_Paper(x,y,n)
                Color_Paper(x,y+n,n)
                Color_Paper(x+n,y,n)
                Color_Paper(x+n,y+n,n)
                return
    if L[x][y] == 0:
        result_zero += 1
    else:
        result_one += 1
    
if __name__ == '__main__':
    Color_Paper(0,0,n)
    print(result_zero)
    print(result_one)