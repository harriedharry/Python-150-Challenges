x = []

for i in range(10):
    x.append("color"+str(i))

a = int(input("Start num: "))
b = int(input("End num: "))

print("Colors between them are: ")

print(x[a:b])
