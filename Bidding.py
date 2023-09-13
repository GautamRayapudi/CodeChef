T=int(input())
while T>0:
    A,B,C=map(int,input().split())
    if (A>B and A>C):
        print("Alice")
    elif (B>A and B>C):
        print("Bob")
    else:
        print("Charlie")
    T-=1