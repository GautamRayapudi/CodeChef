T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    if sum(A)%2 !=0:
        print("YES")
    else:
        print("NO")