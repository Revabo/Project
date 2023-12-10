import sys

n = int(sys.stdin.readline())
dp = [-1 for i in range(10000000)]

def Fibonacci(n):
    if n <= 2: return 1
    
    if dp[n] != -1 : return dp[n]
    else : 
        dp[n] = Fibonacci(n-1) + Fibonacci(n-2)
        return dp[n]

if __name__ == '__main__':
    print(Fibonacci(n))