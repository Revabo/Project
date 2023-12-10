import sys

n = int(sys.stdin.readline())

def Sticker(n):
    for i in range(n):        
        a = int(sys.stdin.readline())
        L = [[],[]]
        dp = [[-1 for _ in range(a)],[-1 for _ in range(a)]]
        
        L[0] = list(map(int,sys.stdin.readline().split()))
        L[1] = list(map(int,sys.stdin.readline().split()))
        
        dp[0][0] = L[0][0]
        dp[1][0] = L[1][0]
        if a >= 2:
            dp[0][1] = L[0][1] + L[1][0]
            dp[1][1] = L[1][1] + L[0][0]
        
        for k in range(2,a):
            dp[0][k] = L[0][k] + max(dp[0][k-2],dp[1][k-1],dp[1][k-2])
            dp[1][k] = L[1][k] + max(dp[1][k-2],dp[0][k-1],dp[0][k-2])
        
        print(max(max(dp[0]),max(dp[1])))
        
if __name__ == '__main__':
    Sticker(n)