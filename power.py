def powerOf(b,e):
    if e<0:
        return 1/b*powerOf(b,e+1)
    elif e>0:
        return b*powerOf(b, e-1)
    else:
        return 1
base= int(input("Enter the base: "))
exp= int(input("Enter the exponent: "))
print(f"{base} to the power {exp}= {powerOf(base,exp)}")