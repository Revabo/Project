import sys

def Assignment(n):
    L = [[0,0] for i in range(n)]
    Clear = [False for _ in range(1001)]
    result = 0
    for i in range(n):
        L[i] = list(map(int,sys.stdin.readline().split()))
    L.sort(key = lambda x : (-x[1],x[0]))
    
    for left_day, score in L:
        for day in range(left_day,0,-1):
            if not Clear[day]:
                Clear[day] = True
                result += score
                break
    return result

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(Assignment(n))