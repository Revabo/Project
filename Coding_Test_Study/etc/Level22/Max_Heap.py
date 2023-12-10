import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
Heap = []

def Max_Heap():
    for i in range(N):
        tmp = int(sys.stdin.readline())
        
        if tmp == 0:
            if not Heap:
                print(0)
            else:
                print(heappop(Heap)[1])
        else:
            heappush(Heap,(-tmp,tmp))
    
if __name__ == '__main__':
    Max_Heap()