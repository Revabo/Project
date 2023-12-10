import sys

gun = ['ChongChong']

n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(str,sys.stdin.readline().split())
    if a in gun :
        gun.append(b)
    elif b in gun :
        gun.append(a)
    
    
gun  = set(gun)
print(len(gun))