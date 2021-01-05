x = []

for i in range(4):
    x.append("Prog"+str(i))

pos = int(input("Where?:"))
pro = input("What?:")

x.insert(pos,pro)

print(x)
