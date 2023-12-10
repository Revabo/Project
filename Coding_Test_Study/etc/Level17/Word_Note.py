import sys

note = {}
count = []
index = 0

a,b  = map(int,sys.stdin.readline().split())
for i in range(a):
    tmp = sys.stdin.readline().rstrip()
    if len(tmp) < b : continue
    if tmp in note : note[tmp] += 1
    else : note[tmp] = 1
    
note = sorted(note.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))

for i in range(len(note)):
    print(note[i][0])