import sys


N = int(sys.stdin.readline())
def Known():
    L = [i for i in range(1,N*2,2)]
    for i in range(len(L)):
        print(L[i], end=' ')
    
if __name__ == '__main__':
    Known()