import math
for T in range(int(input())):
    A=list(map(int,input().split()))
    div=math.gcd(*A)
    print(div)
        