T=int(input())
while T>0:
    N=int(input())
    income=N*50
    profit=income-(0.2+0.2+0.3)*income
    print(int(profit))
    T-=1