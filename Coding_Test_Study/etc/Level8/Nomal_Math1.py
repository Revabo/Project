import sys

t = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def Trans(a, n):
    result = ''
    while a > 0 :
        remain = a % n
        a = a // n
        result = t[remain] + result
    return result

a, n  = map(int,sys.stdin.readline().split())
print(Trans(a, n))