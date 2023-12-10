import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())
Heap = []

def Min_Heap():
    for i in range(N):
        tmp = int(sys.stdin.readline())
        
        if tmp == 0:
            if not Heap:
                print(0)
            else:
                print(heappop(Heap))
        else:
            heappush(Heap,tmp)
    
if __name__ == '__main__':
    Min_Heap()