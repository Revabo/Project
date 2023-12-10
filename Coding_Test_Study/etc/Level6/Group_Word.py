a = int(input())
n = []
count = 0
for i in range(a):
    s = list(input())
    for j in range(len(s)):
        if j != 0 and n[j-1] != s[j] and s[j] in n: break
        n.append(s[j])
        if j+1 == len(s) :
            n = []
            count = count + 1
print(count)

