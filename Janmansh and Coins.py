T=int(input())
while T>0:
    X,Y=map(int,input().split())
    total=X*10+Y*5
    print(total)
    T-=1