import sys

n = int(sys.stdin.readline())
L = [[] for i in range(n)]
Time = [0 for i in range(n)]

def Meeting():
    count = 0
    start = 0
    time = [0,0]
    
    for i in range(n):
        L[i] = list(map(int,sys.stdin.readline().split()))
    L.sort()
    
    for i in range(n-1):
        if start > L[i][0]: 
            Time[i] = L[i][1] - L[i][0]
            tmp = time[1] - time[0]

            if Time[i] < tmp:
                if time[0] - L[i][0] >= Time[i] - tmp:
                    start = L[i][1]
                    time = L[i]
            else:
                continue
        
        else:
            Time[i] = L[i][1] - L[i][0]
            tmp = L[i+1][1] - L[i+1][0]

            if Time[i] > tmp:
                if L[i+1][0] - L[i][0] >= Time[i] - tmp:
                    start = L[i][1]
                    count += 1
                    time = L[i]
            else:
                start = L[i][1]
                count += 1
                time = L[i]
    if start <= L[n-1][0]: count += 1
        
    return count

if __name__ == '__main__':
    print(Meeting())