import math
X,Y=map(int,input().split())
diff=X-Y
yy=math.ceil(Y/2)
sol=diff+yy
print(sol)