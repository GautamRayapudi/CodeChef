T=int(input())
while T>0:
    X1,X2,X3,V1,V2=map(int, input().split())
    if ((X3-X1)/V1<(X2-X3)/V2):
        print("Chef")
    elif((X3-X1)/V1>(X2-X3)/V2):
        print("Kefa")
    else:
        print("Draw")
    T-=1    