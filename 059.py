import random

ch = ["red","blue","green","yellow","black"]

c = random.choice(ch)

a = input("Guess the color: ")

while c != a:
    a = input("Guess again>>>>")

print("Correct")
