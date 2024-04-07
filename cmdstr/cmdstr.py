import execStr as es
l= list()
cmds = list()
n= int(input("Enter the number of commands: "))
for i in range(n):
    inp= input(f"{i+1} ")
    cmds.append(inp)
for i in range(n):
    print(f"{i+1} Command: ", cmds[i])
    print("Output: ",end="")
    es.execStr(cmds[i],l)
    print()

