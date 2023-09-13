T=int(input())
while T>0:
    maxT,maxN,sumN=map(int,input().split())
    q=sumN//maxN
    r=sumN%maxN
    if r==0 and maxT*maxN>sumN:
        print(q*maxN**2)
    elif r!=0 and maxT*maxN>sumN:
        print(q*maxN**2+r**2)
    else:#if maxT*maxN<sumN
        print(maxT*maxN**2)
    T-=1    