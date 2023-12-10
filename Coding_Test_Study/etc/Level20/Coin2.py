import sys

n, k = map(int,sys.stdin.readline().split())

def Coin():
    L = [0 for _ in range(n)]
    Impossible = 10000000000
    Count = [[Impossible for _ in range(10001)] for __ in range(n+1)]
    result = 10000000001
    
    for i in range(n):
        L[i] = int(sys.stdin.readline())
    Count[0][0] = 0
    
    for i in range(1,n+1):
        Count[i][0] = 0
        for j in range(1,k+1):
            if j >= L[i-1]:
                Count[i][j] = min(Count[i-1][j-L[i-1]] + 1, Count[i][j-L[i-1]] + 1, Count[i-1][j])
            else:
                Count[i][j] = Count[i-1][j]
            
    for i in range(1,n+1):
        if result >= Count[i][k]:
            result = Count[i][k]
            
    if result >= Impossible:
        result = -1
    return result

if __name__ == '__main__':
    print(Coin())