import math
T=int(input())
while T>0:
    N,X=map(int,input().split())
    min=(math.ceil(N/6)*X)
    print(min)
    T-=1