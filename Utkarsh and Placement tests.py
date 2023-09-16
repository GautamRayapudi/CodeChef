T=int(input())
while T>0:
    p1,p2,p3=map(str,input().split(' '))
    c1,c2=map(str,input().split(' '))
    if (p1==c1) or (p1==c2):
        print(p1)
    elif (p2==c1) or (p2==c2):
        print(p2)
    else:
        print(p3)
    T-=1    