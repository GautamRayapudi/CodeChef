T=int(input())
while T>0:
    N=int(input())
    a=[]
    i=0
    while i<=N-1:
        if i==0:
            a.append(1)
        elif 0<i<N-1:
            a.append(0)
        else:
            a.append(1)
        i+=1    
    L=''.join(map(str,a))
    print(L)
    T-=1    