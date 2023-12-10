import sys
n = int(sys.stdin.readline())
L = [[] for __ in range(n)]
for i in range(n):
    L[i] = list(map(int, sys.stdin.readline().split()))
result_minus = 0
result_zero = 0
result_plus = 0

def Paper(x,y,n):
    global result_plus, result_zero, result_minus
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if L[x][y] != L[i][j]:
                n = n//3
                Paper(x, y, n)
                Paper(x+n, y, n)
                Paper(x+(n*2), y, n)
                
                Paper(x, y+n, n)
                Paper(x+n,y+n,n)
                Paper(x+(n*2),y+n, n)
                
                Paper(x,y+(n*2),n)
                Paper(x+n,y+(n*2),n)
                Paper(x+(n*2),y+(n*2),n)
                #print(x,y,n,result_minus)
                return
                
    if L[x][y] == -1:
        result_minus += 1
    elif L[x][y] == 0:
        result_zero += 1
    else :
        result_plus += 1

if __name__ == '__main__':
    Paper(0,0,len(L))
    print(result_minus)
    print(result_zero)
    print(result_plus)