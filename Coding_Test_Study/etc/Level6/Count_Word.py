s = input().split(' ')
while '' in s:
    s.remove('')
print(len(s))