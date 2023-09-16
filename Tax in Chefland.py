T=int(input())
sum=0
while T>0:
    X=int(input())
    if X>100:
        sum=X-10
    else:
        sum=X
    print(sum)    
    T-=1