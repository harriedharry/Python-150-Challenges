x = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

for i in range(len(x)):
    for j in range(3):
        print(x[i][j],end = " ")
    print("\n")

row = int(input("Row:"))

for col in range(3):
    print(x[row][col])

col = int(input("Which col:"))
print(x[row][col])


val = int(input("New Value: "))

x[row][col] = val

print(x)
