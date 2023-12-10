import sys

n, m = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

def Cut_Tree():
    Min = 0
    Max = max(L)
    while(Min + 1 < Max):
        Cutting = (Min + Max) // 2
        result = 0
        for i in range(len(L)):
            if L[i] >= Cutting:
                result += L[i] - Cutting
        if result == m:
            return Cutting
        elif result > m :
            Min = Cutting
        else :
            Max = Cutting
    
    return Min
    
if __name__ == '__main__':
    print(Cut_Tree())