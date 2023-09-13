T=int(input())
while T>0:
    A,B,C=map(int,input().split())
    print(max(A,B,C))
    T-=1