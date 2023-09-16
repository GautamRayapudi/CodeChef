T=int(input())
while T>0:
    A,B=map(int, input().split(' '))
    burgers=min(A,B)
    print(burgers)
    T-=1