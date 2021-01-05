from array import *
import random


a = array('i',[])
b = array('i',[])

for i in range(3):
    a.append(random.randint(1,100))

print("Input 5 int:")

for i in range(5):
    z = int(input())
    b.append(z)

a.extend(b)

a = sorted(a)
print(a)
