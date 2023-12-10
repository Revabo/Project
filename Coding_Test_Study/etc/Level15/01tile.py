a = int(input())

tile = [0]*1000000
tile[0] = 1
tile[1] = 2

def Tile(n):
    for i in range(a-2):
        tile[n+i] = tile[n-1+i] + tile[n-2+i]
        tile[n+i] %= 15746
    
Tile(2)

print(tile[a-1])