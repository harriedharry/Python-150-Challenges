from array import *

a = array('i',[2,3,5,9,7])
print(a)

b = int(input("Num:"))
z = 1

while z:
    for i in range(len(a)):
        if b == a[i]:
            print(a.index(b))
            z=0
            break
    print("Try Again")
    b = int(input("Num:"))

