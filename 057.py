import random

c = random.randint(1,10)
a = int(input("Guess: "))


while a != c :
    if a > c :
        print("Too High!")
    else:
        print("Too Low!")

    a = int(input("Guess Again!"))

print("You did it!")
