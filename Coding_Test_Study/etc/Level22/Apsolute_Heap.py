import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())
Heap = []

def Apsolute_Heap():
    for i in range(N):
        tmp = int(sys.stdin.readline())
        
        if tmp == 0:
            if not Heap:
                print(0)
            else:
                print(heappop(Heap)[1])
        else:
            heappush(Heap,(abs(tmp),tmp))
    
if __name__ == '__main__':
    Apsolute_Heap()