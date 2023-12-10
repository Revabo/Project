import sys

a = int(sys.stdin.readline().strip())
wmax = hmax = 0
tmp = list()
lenth = [0]*6
for i in range(6):
    tmp = list(map(int,sys.stdin.readline().split()))
    lenth[i] = tmp[1]
    if tmp[0] in [1,2]:
        if wmax < tmp[1]:
            wmax = tmp[1]
    else:
        if hmax < tmp[1]:
            hmax = tmp[1]

subw = abs(lenth[lenth.index(wmax)-1] - lenth[lenth.index(wmax)+1])
subh = abs(lenth[lenth.index(hmax)-1] - lenth[lenth.index(hmax)+1])
area = (wmax * hmax) - (subw * subh)
print(area*a)