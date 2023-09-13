N = int(input())
for _ in range(N):
    # M = int(input())
    A,B,C = map(int,input().split())
    # Y = list(map(int,input().split()))
    if (min(A,B) == min(B,C) == min(C,A)):
        print("Yes")
    else:
        print("No")