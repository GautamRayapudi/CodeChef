T=int(input())
while T>0:
    A,B,C=map(int,input().split())
    if ((A+B+C)>=100 and A>=10 and B>=10 and C>=10):
        print("PASS")
    else:
        print("FAIL")
    T-=1