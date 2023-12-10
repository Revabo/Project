from itertools import combinations

a = int(input())
t = [i+1 for i in range(a)]
s = []
min = 9999999999999
for i in range(a):
    tmp = list(map(int,input().split()))
    s.append(tmp)
team = list(combinations(t,a//2))

def Team(start,link):
    global min
    st = team[start]
    lt = team[link]
    ss = ls = 0
    for i in range(len(st)):
        for j in range(len(st)):
            ss += s[st[i]-1][st[j]-1]
            ls += s[lt[i]-1][lt[j]-1]
    dif = abs(ss-ls)
    if dif < min:
        min = dif
for i in range(len(team)//2):
    Team(0+i,len(team)-i-1)
print(min)