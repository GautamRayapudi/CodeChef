T = int(input())
while T>0:
    N = int(input())
    if N>=7:
        print("YES")
    if (1<=N<7):
        if N%2 == 0:
            print("YES")
        else:
            print("NO")
    T-=1        
        