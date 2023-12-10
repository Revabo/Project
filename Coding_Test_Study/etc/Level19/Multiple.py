import sys

a,b,c = map(int,sys.stdin.readline().split())

def Mul(a,b):
    if b == 1 : 
        return a % c
    else:
        tmp = Mul(a,b//2)
        if b % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

if __name__ == '__main__':
    print(Mul(a,b))