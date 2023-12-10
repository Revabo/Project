import sys

n = int(sys.stdin.readline())

def ATM():
    prepix_sum = [0 for _ in range(n)]
    m = list(map(int,sys.stdin.readline().split()))
    m.sort()
    
    for i in range(n):
        prepix_sum[i] = prepix_sum[i-1] + m[i]
    
    return sum(prepix_sum)

if __name__ == '__main__':
    print(ATM())