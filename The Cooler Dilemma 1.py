import math
T=int(input())
while T>0:
    X,Y,M=map(int,input().split())
    rent = math.ceil(Y/X)
    if rent>M:
        print("YES")
    else:
        print("NO")
    T-=1    