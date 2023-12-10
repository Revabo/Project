import sys

A = int(sys.stdin.readline())
for a in range(A) : # int(input())을 바로 range안에 넣기도 가능
    B, C = map(int, sys.stdin.readline().split())
    print(B+C)