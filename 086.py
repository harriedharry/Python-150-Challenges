a = input("Password:")
b = input("Password:")


if a == b:
    print("Thank You")
elif a.lower() == b.lower() and a != b:
    print("They must be in the same case")
else:
    print("Incorrect!")


