import math
T=int(input())
while T>0:
    X,Y=map(int,input().split())
    print(math.floor(X/Y))
    T-=1
    