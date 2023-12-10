s = input().upper()
a = list(set(s))
b = []
for i in a:
    b.append(s.count(i))
if b.count(max(b)) > 1 : print('?')
else : print(a[b.index(max(b))])