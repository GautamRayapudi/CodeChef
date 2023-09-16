T=int(input())
while T>0:
    G1,S1,B1,G2,S2,B2=map(int, input().split())
    if G1+S1+B1>G2+S2+B2:
        print("1")
    else:
        print("2")
    T-=1    