import sys
from itertools import combinations

def Subsequence():
    Count = 0
    tmp = 0
    result = []
    N, S = map(int,sys.stdin.readline().split())
    L = list(map(int,sys.stdin.readline().split()))
    for i in range(N+1):
        result += combinations(L,i)
    for i in range(1,len(result)):
        if sum(result[i]) == S:
            Count += 1
    return Count

if __name__ == '__main__':
    print(Subsequence())