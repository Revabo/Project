import sys

n, m = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
    
def Guitar():
    Max = sum(L)
    Min = 1
    Ans = 10000000000
    while(Min <= Max):
        Mid = (Max + Min) // 2
        result = 1
        length = 0
        
        for i in range(n):
            if length + L[i] <= Mid:
                length += L[i]
            else:
                length = L[i]
                result += 1
            #print(Ans,Max,Min,Mid,result,length)
        
        if result > m:
            Min = Mid + 1
        else:
            Max = Mid - 1
            Ans = min(Ans,Mid)
            
    if max(L) <= Ans:
        return Ans
    else:
        return max(L)
    
if __name__ == '__main__':
    print(Guitar())