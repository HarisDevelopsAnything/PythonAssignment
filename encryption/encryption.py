import encrypter as enc
inp = input("Enter the string to decrypt: ").upper()
dec= enc.encrypt(inp)
print(dec)