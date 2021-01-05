import random

x = []

for i in range(4):
    x.append(random.randint(101,999))

y = int(input("Enter a 3 digit num: "))

for i in range(4):
    if y == x[i]:
        print("This is on",i,"position")

print("That number is not on the list")


