T=int(input())
while T>0:
    X,Y,Z=map(int, input().split())
    if X+Y<=Z:
        print("YES")
    else:
        print("NO")
    T-=1    