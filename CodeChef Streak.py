T=int(input())
while T>0:
    N=int(input())
    O=list(map(int,input().split()))
    A=list(map(int,input().split()))
    Ocount=0
    Acount=0
    Ostreak=Ocount
    Astreak=Acount
    for i in range(N):
        if O[i]>0:
            Ocount+=1
        else:
            Ocount=0
        if A[i]>0:
            Acount+=1
        else:
            Acount=0
        Astreak=max(Acount,Astreak)
        Ostreak=max(Ocount,Ostreak)
    if Astreak>Ostreak:
        print("Addy")
    elif Ostreak>Astreak:
        print("Om")
    else:
        print("Draw")
    T-=1