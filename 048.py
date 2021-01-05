a = input("Do you want to invite someone? :")
c = 0

while a != "no":
    b = input("What's the name: ")
    print(b," has been invited.")
    a = input("Do you want to invite someone? :")
    c +=1

print(c," people are coming.")
