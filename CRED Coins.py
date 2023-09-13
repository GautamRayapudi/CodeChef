T=int(input())
while T>0:
    X,Y=map(int,input().split())
    cred=X*Y
    print(cred//100)
    T-=1