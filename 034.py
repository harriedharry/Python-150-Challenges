print('''1) Squares
2) Triangle''')
a = int(input("Enter a num: "))
if a == 1:
    s = int(input("Enter the side "))
    print("Area = ",s*s)
elif a == 2:
    b = int(input("Enter the base "))
    h = int(input("Enter the height "))
    print("Area = ", 0.5 * b *h)
else:
    print("Go to Hell!")
