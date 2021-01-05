
a = input("Up or Down: ")
a = a.lower()
if a == "down":
    b = int(input("top num: "))
    for i in range(b,0,-1):
        print(i)
elif a == "up":
    b = int(input("num: "))
    for i in range(1,b+1):
        print(i)
else:
    print("I don't understand.")

