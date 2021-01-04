a = int(input("What's your age:"))
if a == 18:
    print("You can vote")
elif a == 17:
    print("You can drive")
elif a == 16:
    print("You can buy a lottery ticket")
elif a < 16:
    print("You can go trick-or-treating")
else:
    print("You are too old")
