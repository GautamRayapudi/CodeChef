T=int(input())
while T>0:
    N,X=map(int,input().split())
    if N<=X and X%N==0:
        print("YES")
    else:
        print("NO")
    T-=1