import sys

n = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())


def Budget():
    Min = 0
    Max = max(L)
    ans = 0
    while(Min <= Max):
        Mid = (Min + Max) // 2
        result = 0
        for i in range(len(L)):
            if Mid >= L[i]:
                result += L[i]
            else:
                result += Mid
        
        if result == m:
            return Mid
        elif result > m:
            Max = Mid - 1
        else:
            Min = Mid + 1
            ans = max(ans,Mid)
    
    return ans
    
    
if __name__ == '__main__':
    print(Budget())