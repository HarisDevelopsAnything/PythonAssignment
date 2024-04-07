alphabets= [chr(i) for i in range(65,91)]
alphabets.extend(alphabets)
def encrypt(inp):
    dec= ""
    for i in inp:
        if i.isalpha():
            dec+= alphabets[(alphabets.index(i)+3)]
        else:
            dec+= i
    return dec