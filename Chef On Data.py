T = int(input())
while T>0:
    X,Y=map(int,input().split())
    if X>=Y:
        print("YES")
    else:
        print("NO")
    T-=1