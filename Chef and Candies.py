import math
T=int(input())
while T>0:
    N,X=map(int,input().split())
    if X>=N:
        print(0)
    else:
        min = (N-X)/4
        print(math.ceil(min))
    T-=1    