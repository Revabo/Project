import sys

n, c = map(int, sys.stdin.readline().split())
L = [-1 for _ in range(n)]
for i in range(n):
    L[i] = int(sys.stdin.readline())
L.sort()

def Set_Wifi():
    Max = L[n-1] - L[0]
    Min = 1
    Ans = 0
    while(Min <= Max):
        Mid = (Max + Min) // 2
        result = 1
        Current = L[0]
        
        for i in range(n):
            if L[i] >= Current + Mid:
                result += 1
                Current = L[i]
                
        if result >= c:
            Min = Mid + 1
            Ans = max(Ans, Mid)
        else:
            Max = Mid - 1
    return Ans

if __name__ == '__main__':
    print(Set_Wifi())