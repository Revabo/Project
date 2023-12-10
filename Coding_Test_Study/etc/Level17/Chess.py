import sys


def Chess(Color,L):
    prepix_sum = [[0 for i in range(m+1)] for i in range(n+1)]
    tmp = 0
    min = 100000000000000000
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0:
                if L[i][j] != Color: tmp = 1
                else : tmp = 0
            else :
                if L[i][j] == Color: tmp = 1
                else : tmp = 0
            prepix_sum[i+1][j+1] = prepix_sum[i][j+1] + prepix_sum[i+1][j] - prepix_sum[i][j] + tmp
    
    for i in range(1,n-k+2):
        for j in range(1,m-k+2):
            tmp = prepix_sum[i+k-1][j+k-1] - prepix_sum[i+k-1][j-1] - prepix_sum[i-1][j+k-1] + prepix_sum[i-1][j-1]
            if tmp < min :
                min = tmp
    return min
    
if __name__ == '__main__':
    n, m, k = map(int,sys.stdin.readline().split())
    L = [list(sys.stdin.readline().rstrip()) for i in range(n)]
    print(min(Chess('B',L),Chess('W',L)))