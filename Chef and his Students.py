for T in range(int(input())):
    count=0
    l=input()
    for i in range(len(l)-1):
        if l[i] == '<' and l[i+1] == '>':
            count=count+1
    print(count)