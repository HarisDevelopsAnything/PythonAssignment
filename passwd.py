import random
chrs= list()
ucl= [chr(i) for i in range(65,91)]
lcl= [chr(i) for i in range(97,123)]
dig= [i for i in range(0,10)]
symbols= ['!','@','#','$']
chrs.extend(ucl)
chrs.extend(lcl)
chrs.extend(dig)
chrs.extend(symbols)
pwd= ""
l= int(input("Enter the length of password to generate: "))
for i in range(l):
    pwd+= str(random.choice(chrs))
print("Password: ", pwd)