T=int(input())
while T>0:
    A,B,X,Y=map(int,input().split())
    if A*B<=X*Y:
        print("Yes")
    else:
        print("No")
    T-=1    