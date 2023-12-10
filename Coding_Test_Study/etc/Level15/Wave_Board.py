a = int(input())
wave = [0]*101
wave[0] = wave[1] = wave[2] = 1

def P(n):
    global b
    if n > b:
        return
    wave[n] = wave[n-2] + wave[n-3]
    P(n+1)

for i in range(a):
    b = int(input())
    P(3)
    print(wave[b-1])