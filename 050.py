
guess = int(input("Guess the num: "))
while not (guess > 10 and guess < 20) :
    if guess < 10 :
        print("Too LOW!")
    elif guess > 20 :
        print("Too HIGH!")
    guess = int(input("Guess the num: "))


print("Congratulation!!")

