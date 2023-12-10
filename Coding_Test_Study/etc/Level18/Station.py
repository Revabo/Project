import sys

n = int(sys.stdin.readline())

def Station():
    Vector = list(map(int, sys.stdin.readline().split()))
    Price = list(map(int, sys.stdin.readline().split()))
    Min = 10000000000
    result = 0
    
    for i in range(n-1):
        if Price[i] <= Min:
            Min = Price[i]
        result += Min * Vector[i]
        
    return result

if __name__ == '__main__':
    print(Station())