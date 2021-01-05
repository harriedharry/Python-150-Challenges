from array import *

a = array('f',[1.23,5.43,2.43,4.89,6.23])

c = True

while c:
    num = int(input("Enter a num in the range of 2 and 5:"))
    if num >=2 and num <= 5:
        c = False


for i in a:
    print(round(i/num,2))
