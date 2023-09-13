T=int(input())
for i in range(T):
    N=int(input())
    pairs=[]
    for j in range(N):
        c=int(input())
        if c not in pairs:
            pairs.append(c)
        else:
            pairs.remove(c)
    print(pairs[0])        