import sys

a = list(map(int,sys.stdin.readline().split()))
while 0 not in a:
    if a[1]%a[0]==0:
        print('factor')
    elif a[0]%a[1]==0:
        print('multiple')
    else:
        print('neither')
    a = list(map(int,sys.stdin.readline().split()))