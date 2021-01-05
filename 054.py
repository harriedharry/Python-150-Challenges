import random

c = ["h","t"]

g = input("Select b/w h and t:")
z = random.choice(c)

if g == z:
    print("You win")
else:
    print("Bad Luck.","Computer chose",z)
