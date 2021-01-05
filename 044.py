a = int(input("How many people do you want to invite: "))
if a > 10:
    print("Too many people.")
else:
    for i in range(a):
        s = input("What's the name: ")
        print(s.capitalize(),"has been invited.")
