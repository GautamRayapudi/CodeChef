T=int(input())
while T>0:
    a,b,c,d=map(int,input().split())
    S1=a+b
    S2=c+d
    if S1>S2:
        print(S2)
    elif S1<S2:
        print(S1)
    else:
        print(S1)
    T-=1    