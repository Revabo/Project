import sys

a = list(map(int,sys.stdin.readline().split()))
gcda = set()
gcdb = set()
lcma = list([a[0]])
lcmb = list([a[1]])

for i in range(1,a[0]+1):
    if a[0]%i==0:
        gcda.add(i)
for i in range(1,a[1]+1):
    if a[1]%i==0:
        gcdb.add(i)
print(max(gcda&gcdb))

i = 2
while lcma[0]*i <= lcma[0]*lcmb[0]:
    lcma.append(lcma[0]*i)
    i += 1
i = 2
while lcmb[0]*i <= lcma[0]*lcmb[0]:
    lcmb.append(lcmb[0]*i)
    i += 1
lcma = set(lcma)
lcmb = set(lcmb)
print(min(lcma&lcmb))