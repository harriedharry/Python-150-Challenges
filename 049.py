a = 50
guess = int(input("Guess the num: "))
while guess != a:
    if guess < 50 :
        print("Too LOW!")
    elif guess > 50 :
        print("Too HIGH!")
    guess = int(input("Guess the num: "))


print("Congratulation!!")

