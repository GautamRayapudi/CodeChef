T=int(input())
while T>0:
    N,K,M=map(int,input().split())
    if K*M>=N:
        print(1)
    elif N%(K*M)==0:
        print(N//(K*M))
    else:
        print((N//(K*M)+1))
    T-=1