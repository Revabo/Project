import sys

n, m = map(int,sys.stdin.readline().split())
L = [0 for i in range(n)]

def Coin(money):
    count = 0
    for i in range(n):
        L[i] = int(sys.stdin.readline().rstrip())
    
    for i in range(n-1,-1,-1):
            count += money // L[i]
            money %= L[i]
    return count

if __name__ == '__main__':
    print(Coin(m))