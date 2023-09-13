# cook your dish here
T=int(input())
while T>0:
    count=0
    N=int(input())
    S=str(input())
    for i in S:
        if (i!='a' and i!='e' and i!='i' and i!='o' and i!='u'):
            count+=1
            if count==4:
                print("NO")
                break
        else:
            count=0
    if count<4:
        print("YES")
    T-=1    
                
                
    
                