T=int(input())
while T>0:
    X,Y=map(int, input().split(' '))
    Hours=Y-X
    print(Hours)
    T-=1