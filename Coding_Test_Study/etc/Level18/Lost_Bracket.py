import sys

def Bracket():
    tmpn = ''
    sign = ''
    flag = 0
    result = 0
    num = 0
    
    L = str(sys.stdin.readline().rstrip())
    for i in range(len(L)):
        if 47 < ord(L[i]) < 58:
            tmpn += L[i]
            
        elif ord(L[i]) == 45:
            if sign == '':
                result = int(tmpn)
            elif sign == '+':
                if flag == 1:
                    num += int(tmpn)
                    result -= num
                    num = 0
                else :
                    result += int(tmpn)
            elif sign == '-':
                num += int(tmpn)
                result -= num
                num = 0
            tmpn = ''
            sign = '-'
            flag = 1
            
        elif ord(L[i]) == 43:
            if sign == '':
                result = int(tmpn)
            elif sign == '+':
                if flag == 1:
                    num += int(tmpn)
                else :
                    result += int(tmpn)
            elif sign == '-':
                num = int(tmpn)
            tmpn = ''
            sign = '+'
        #print(tmpn,sign,flag,result)
    if sign == '+':
        if flag == 1:
            num += int(tmpn)
            result -= num
        else:
            result += int(tmpn)
    elif sign == '':
        result = int(tmpn)
    else:
        result -= int(tmpn)
        
    return result
    
if __name__ == '__main__':
    print(Bracket())