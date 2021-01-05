from array import *

a = array('i',[])
l = 0


while l != 5:
    x = int(input("Enter a NUM:"))
    if x >=10 and x <= 20:
        a.append(x)
        l +=1
    else:
        print("Out of Range")

for i in range(5):
    print(a[i])
