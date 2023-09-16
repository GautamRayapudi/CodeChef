T=int(input())
while T>0:
    N,K=map(int,input().split())
    
    H=list(map(int,input().split(" ")))
    c=0
    
    for i in range(N):
        if(H[i] > K):
            c+=1
    print(c)
    T-=1