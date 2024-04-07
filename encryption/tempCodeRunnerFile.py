alphabets= [chr(i) for i in range(65,91)]
inp = input("Enter the string to decrypt: ").upper()
dec= ""
for i in inp:
    if i.isalpha():
        dec+= alphabets[(alphabets.index(i)+3) if (alphabets.index(i)+3) < len(alphabets) else alphabets[::1].index(i)]
    else:
        dec+= i
print(dec)