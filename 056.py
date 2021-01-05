import random

c = random.randint(1,10)
a = int(input("Guess: "))


while a != c :
    a = int(input("Guess Again!:"))

print("You did it!")
