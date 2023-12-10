import sys

def Cantor(a):
    if len(a) == 1 : return '-'
    div = len(a) // 3
    return Cantor(a[0:div])+ ' ' * div+ Cantor(a[div*2 - 1:-1])
    
if __name__ == '__main__':
    while (1):
        a = sys.stdin.readline().rstrip()
        if a == '':
            break
        tmp = '-' * (3**int(a))
        print(Cantor(tmp))