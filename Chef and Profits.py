T=int(input())
while T>0:
    X,Y,Z=map(int, input().split())
    profit=(X*Z)-(X*Y)
    print(profit)
    T-=1