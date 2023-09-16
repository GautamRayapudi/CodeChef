T=int(input())
while T>0:
    X,N=map(int, input().split(' '))
    score=(X//10)*N
    print(score)
    T-=1