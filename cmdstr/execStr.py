def execStr(s,l):
    sep= s.split(sep= " ")
    if "insert" in s:
        if(len(sep)!=3):
            print("Invalid syntax for insert")
        else:
            l.insert(int(sep[1]),int(sep[2]))
            print()
    elif "remove" in s:
        if(len(sep)!=2):
            print("Invalid syntax for remove")
        else:
            l.remove(int(sep[1]))
    elif "append" in s:
        if(len(sep)!=2):
            print("Invalid syntax for append")
        else:
            l.append(int(sep[1]))
    elif "pop" in s:
        if(len(sep)!=1):
            print("Invalid syntax for pop")
        else:
            l.pop()
    elif "sort" in s:
        if(len(sep)!=1):
            print("Invalid syntax for sort")
        else:
            l.sort()
    elif "reverse" in s:
        if(len(sep)!=1):
            print("Invalid syntax for reverse")
        else:
            l=l.reverse()
    elif s=="print":
        print(l)

    