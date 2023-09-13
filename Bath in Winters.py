import math
T=int(input())
while T>0:
    X,Y=map(int,input().split())
    prod=2*Y
    print(math.floor(X/prod))
    T-=1