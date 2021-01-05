from array import *

a = array('i',[])

for i in range(5):
    a.append(int(input()))

a = sorted(a)
a.reverse()


print(a)

