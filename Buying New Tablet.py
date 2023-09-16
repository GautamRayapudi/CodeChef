for T in range(int(input())):
    s=[]
    n,b=list(map(int,input().split()))
    for i in range(n):
        w,h,p=list(map(int,input().split()))
        if(p<=b):
            s.append(w*h)
    if len(s)==0:
        print("no tablet")
    else:
        print(max(s))