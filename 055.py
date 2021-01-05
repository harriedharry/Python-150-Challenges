import random


c = random.randint(1,5)
a = int(input("Choose b/w 1 and 5:"))

if a == c:
    print("Well Done!")
else:
    if a > c:
        print("Too HIGH")
    else :
        print("Too LOW")

    a = int(input("Choose Again: "))
    if a == c:
        print("Correct")
    else:
        print("You Lose")



