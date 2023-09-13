T=int(input())
while T>0:
    a,b,c,d=map(int,input().split())
    A=max(a,b)
    C=max(c,d)
    if C>A:
        print("P")
    elif A>C:
        print("Q")
    else:
        print("TIE")
    T-=1    