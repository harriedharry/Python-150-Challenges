import random


score = 0
for i in range(5):
    a = random.randint(1,50)
    b = random.randint(1,50)
    c = a + b
    g = int(input("Your Guess: "))
    if g == c:
        score += 1


print("You Scored",score)
