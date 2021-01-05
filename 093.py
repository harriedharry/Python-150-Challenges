from array import *

original = array('i',[])

print("Enter 5 integer:")

for i in range(5):
    a = int(input())
    original.append(a)

original = sorted(original)

print(original)

z = int(input("Select one of the number to remove:"))


original.remove(z)

print(original)

