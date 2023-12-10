import sys

k, n = map(int, sys.stdin.readline().split())
L = [-1 for _ in range(k)]
for i in range(k):
    L[i] = int(sys.stdin.readline())

def Cut_Lan():
    Max = max(L)
    Min = 1
    Ans = 0
    while(Min <= Max):
        result = 0
        Mid = (Max + Min) // 2
        
        for i in range(k):
            if L[i] >= Mid:
                result += L[i] // Mid
        
        if result >= n:
            Min = Mid + 1
            Ans = max(Ans, Mid)
        else:
            Max = Mid - 1
            
    return Ans
    
if __name__ == '__main__':
    print(Cut_Lan())