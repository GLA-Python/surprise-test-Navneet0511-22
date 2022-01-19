def expanding(lst):
    lst2=[]
    for i in range(1, len(lst)):
        d=lst[1]-[1-1]
        lst2.append(abs(d))
    o=True
    for i in range(1, len(lst2)):
        if lst2[i]<=lst2[i-1]:
            o=False
            break

        return o

    lst=list(map(int,input().split()))
    print(expanding(lst))
