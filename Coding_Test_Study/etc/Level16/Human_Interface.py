import sys

s = sys.stdin.readline()
n = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] for _ in range(len(s))]
for i in range(len(s)-1):
    for j in range(26):
    	n[i][j] = n[i-1][j]
    n[i][ord(s[i])-97] += 1
a = int(sys.stdin.readline())
for i in range(a):
    b = list(sys.stdin.readline().split())
    tmp = ord(b[0]) - 97
    print(n[int(b[2])][tmp] - n[int(b[1])-1][tmp])