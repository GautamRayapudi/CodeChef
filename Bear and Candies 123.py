T=int(input())
while T>0:    
    l,b=map(int,input().split())
    tl=0
    tb=0
    count=0
    while tl<=l and tb<=b:
        count+=1   
        tl=tl+count
        count+=1   
        tb+=count
    if tl>l and tb>b:
        print("Bob")
    elif tl>l:
        print("Bob")
    else:
        print("Limak")
    T-=1    
        