def oesort(l):
    even= [l[i] for i in range(len(l)) if i%2!=0]
    odd= [l[i] for i in range(len(l)) if i%2==0]
    odd.sort()
    even.sort(reverse=True)
    c=0
    d=0
    for i in range(len(l)):
        if i%2!=0:
            l[i]= even[c]
            c+=1
        else:
            l[i]= odd[d]
            d+=1

