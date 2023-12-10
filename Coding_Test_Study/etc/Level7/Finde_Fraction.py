a = int(input())
line = 1
while a > line:
    a -= line
    line += 1
a -= 1
if line % 2 == 0 :
    x = line - a
    y = 1 + a
else :
    y = line - a
    x = 1 + a
print(y,'/',x,sep='')