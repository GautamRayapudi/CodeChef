T=int(input())
while T>0:
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    B=[]
    for j in range(N):
        if A[j]<=K:
            B.append("1")
            K=K-A[j]
        else:
            B.append("0")
    C=''.join(map(str,B))
    print(C)
    T-=1    
            