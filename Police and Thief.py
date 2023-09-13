T=int(input())
while T>0:
    X,Y=map(int,input().split())
    if Y>X:
        print(Y-X)
    elif X>Y:
        print(X-Y)
    else:
        print(0)
    T-=1    