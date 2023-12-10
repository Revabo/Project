import sys
from itertools import permutations

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x : -x[1])
com = [1,2,3,4,5,6,7,8,9]
ans = []

for per in permutations(com,3):
    ans.append(per)
    
    for i in range(len(arr)):
        sk = arr[i][1]
        tmps = 0
        ball = arr[i][2]
        tmpb = 0
        
        for j in range(3):
            if per[j] == int(str(arr[i][0])[j]):
                tmps += 1
            elif str(per[j]) in str(arr[i][0]):
                tmpb += 1
                
                
        if not(tmps == sk and tmpb == ball):
            if per in ans:
                ans.remove(per)
                
print(len(ans))