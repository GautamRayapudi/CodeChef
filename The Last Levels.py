T=int(input())
while T>0:
    X,Y,Z=map(int,input().split())
    if X%3==0:
        s=(X//3)-1
        print(X*Y+s*Z)
    else:
        S=X//3
        W=X*Y+S*Z
        print(W)
    T-=1    